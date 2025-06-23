# 12. Напишите метод, заменяющий в строке все вхождения слова «бяка» на «вырезано цензурой».

def censor_string(text):
    """Заменяет все вхождения слова 'бяка' на 'вырезано цензурой'."""
    censored_text = text.replace("бяка", "вырезано цензурой")
    return censored_text


original_phrase = "Какая же ты бяка, снова съел всю еду. Ну просто бяка!"
result = censor_string(original_phrase)

print("Оригинал:", original_phrase)
print("Результат:", result)
