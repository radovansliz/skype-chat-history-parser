import json
from datetime import datetime
from collections import defaultdict
import argparse
import os

def parse_skype_json(input_file: str, output_file: str = "skype_export.txt"):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    messages_by_date = defaultdict(list)

    for conversation in data.get("conversations", []):
        for message in conversation.get("MessageList", []):
            content = message.get("content", "").strip()
            if not content:
                continue

            if message.get("messagetype", "").startswith("Event") or "URIObject" in content:
                continue

            time_str = message.get("originalarrivaltime")
            try:
                dt = datetime.fromisoformat(time_str.replace("Z", "+00:00"))
                date_key = dt.date().isoformat()
            except:
                continue

            sender = message.get("displayName") or "Me"
            messages_by_date[date_key].append(f"{sender}: {content}")

    output_lines = []
    for date in sorted(messages_by_date.keys()):
        output_lines.append(f"{'-'*7} {date} {'-'*7}")
        output_lines.extend(messages_by_date[date])
        output_lines.append("")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    print(f"✅ Done! Output saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse exported Skype message history JSON into readable TXT.")
    parser.add_argument("-i", "--input", required=True, help="Path to Skype JSON file (e.g. messages.json)")
    parser.add_argument("-o", "--output", default="skype_export.txt", help="Output text file name (default: skype_export.txt)")
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print(f"❌ File not found: {args.input}")
    else:
        parse_skype_json(args.input, args.output)
