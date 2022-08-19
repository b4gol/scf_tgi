def changed(func):
    def change(*args, **kwargs):
        text = "True"
        # with open("out_checker.txt", "r", encoding="utf-8") as file:
        #     text = file.read()
        if bool(text):
            return func(*args, **kwargs)

    return change


@changed
def function(i, j):
    print(i+j)


function(1, 2)
