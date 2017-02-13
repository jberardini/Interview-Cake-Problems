def reverse_message(message):

	words = message.split(" ")

	for i in range(len(words)/2):
		words[i], words[len(words) - i - 1] = words[len(words) - i - 1], words[i]

	return " ".join(words)

print reverse_message("trapped I'm help")


def reverse_chars(phrase):

	for i in range(len(phrase)/2):
		phrase[i], phrase[len(phrase) - i - 1] = phrase[len(phrase) - i - 1], phrase[i]

	return "".join(phrase)


def reverse_message_ic(phrase):

	