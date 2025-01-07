from openai import OpenAI
from openai import APIError, RateLimitError, AuthenticationError, APIConnectionError

def get_openai_response(user_message, openai_api_key):
    """
    Use OpenAI's Chat Completion API to generate a response to the user message.
    """
    try:
        # Create a client with the provided API key
        client = OpenAI(api_key=openai_api_key)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
            ],
            max_tokens=50,  # Adjust token usage
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    except RateLimitError:
        return "Error: You have exceeded your API quota. Please check your plan and usage."
    except AuthenticationError:
        return "Error: Invalid API key. Please check your configuration."
    except APIConnectionError:
        return "Error: Unable to connect to OpenAI API. Please check your network."
    except APIError as e:
        return f"API Error: {e}"
    except Exception as e:
        return f"Unexpected Error: {e}"
