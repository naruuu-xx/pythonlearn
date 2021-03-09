import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors) :
    line = language_file.readine()

    if line :
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


    def print_line(line, encoding, errors) :
        next_lang = line_stirp()
        raw_bytes = next_lang.encode(encoding, errors = errors)
        cooked_string = raw_bytes.decode(encoding, errors = errors)

        print(raw_bytes, "<===>",cooked_string)


    language = open("language.txt",encoding = "utf-8")

    main(languages, encoding, error)
