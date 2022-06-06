import imagegen
import instagramPost


def main(prompt):
    imagegen.run(prompt)
    # instagramPost.post("progress.png", prompt)


if __name__ == '__main__':
    main("lilac | cherry")
