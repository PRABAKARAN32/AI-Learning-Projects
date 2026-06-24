def format_output(content):
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts = []

        for block in content:
            if isinstance(block, dict):
                text = block.get("text")
                if text:
                    parts.append(text.strip())

        return "\n".join(parts)

    return str(content)