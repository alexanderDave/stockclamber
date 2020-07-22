import io

if __name__ == '__main__':
    with open('texts.hcc', 'rb') as f:
        words = f.__sizeof__()

        print(words)