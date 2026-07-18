def parse_response(response):

    # Normal string response
    if isinstance(response.content, str):
        return response.content


    # Gemini structured response
    if isinstance(response.content, list):

        text_parts = []

        for item in response.content:

            if isinstance(item, dict):

                if item.get("type") == "text":

                    text_parts.append(
                        item.get("text", "")
                    )

        return "\n".join(text_parts)


    # Fallback
    return str(response.content)