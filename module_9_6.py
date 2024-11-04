def all_variants(text):
    variants = len(text)

    for start in range(variants):
        for end in range(start + 1, variants + 1):
            yield text[start:end]


a = all_variants("abc")
for i in a:
    print(i)