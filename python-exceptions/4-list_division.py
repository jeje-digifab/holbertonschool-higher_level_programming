#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    div = []
    for i in range(list_length):
        if i >= len(my_list_1) or i >= len(my_list_2):
            print("{:s}".format("out of range"))
            div.append(0)
        else:
            number1 = isinstance(my_list_1[i], (int, float))
            number2 = isinstance(my_list_2[i], (int, float))
            if number1 and number2:
                if my_list_2[i] == 0:
                    print("{:s}".format("division by 0"))
                    div.append(0)
                else:
                    try:
                        result = my_list_1[i] / my_list_2[i]
                        div.append(result)
                    except TypeError:
                        print("{:s}".format("wrong type"))
                        div.append(0)
                    finally:
                        pass
            else:
                print("{:s}".format("wrong type"))
                div.append(0)
    div.extend([0] * (list_length - len(div)))
    return div


if __name__ == "__main__":
    main()
