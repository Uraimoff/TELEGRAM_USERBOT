from services.openai_service import get_openai_response

async def handle_message(event):
    user_message = event.message.message  # Kiruvchi xabarni olish
    try:
        # OpenAI API orqali javob olish
        response = get_openai_response(user_message)
        await event.reply(response)  # Javobni foydalanuvchiga qaytarish
    except Exception as e:
        await event.reply(f"Xatolik yuz berdi: {str(e)}")
