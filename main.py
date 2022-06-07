import imagegen
import instagramPost
import prompt_maker


def run(prompt):
    imagegen.run(prompt)
    instagramPost.post(prompt)


def main():
    run(prompt_maker.get_phrase())


if __name__ == '__main__':
    main()
