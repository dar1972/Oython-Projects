"""
filename: html_builder.py
Language: Python3
name: Dhruv Rajpurohit
Description: The program generates a web page in two different methods
"""
import turtle

def init():
    """
    The funtion initiates the turtle window
    :return:
    """
    turtle.ht()
    turtle.up()
    turtle.title("Font Options")
    turtle.setup(200, 180)
    turtle.setpos(0, 60)
    turtle.delay(0)


def line_turtle():
    """
    The function is to move the turtle to the next line
    :return:
    """
    turtle.rt(90)
    turtle.fd(20)
    turtle.lt(90)


def turtle_dialog_box():
    """
    The function makes the pop-up dialog box with fonts written in it
    :return:
    """
    init()
    turtle.write("Arial", move=False, align="center", font=("Arial", 10, "normal"))
    line_turtle()
    turtle.write("Times New Roman", move=False, align="center", font=("Times New Roman", 10, "normal"))
    line_turtle()
    turtle.write("Comic Sans MS", move=False, align="center", font=("Comic Sans MS", 10, "normal"))
    line_turtle()
    turtle.write("Lucida Grande", move=False, align="center", font=("Lucida Grande", 10, "normal"))
    line_turtle()
    turtle.write("Tahoma", move=False, align="center", font=("Tahoma", 10, "normal"))
    line_turtle()
    turtle.write("Verdana", move=False, align="center", font=("Verdana", 10, "normal"))
    line_turtle()
    turtle.write("Helvetica", move=False, align="center", font=("Helvetica", 10, "normal"))
    turtle.done()


def color_check(inp):
    """
    The function is used to check if the color in the list
    :param inp: input from the user
    :return: boolean
    """
    colors = {'peachpuff', 'slateblue', 'powderblue', 'lightcyan', 'chartreuse', 'moccasin', 'mediumseagreen',
              'lawngreen', 'seagreen', 'mintcream', 'azure', 'goldenrod', 'lightblue', 'firebrick', 'lightseagreen',
              'chocolate', 'yellowgreen', 'darkolivegreen', 'violet', 'ivory', 'sandybrown', 'wheat', 'mediumvioletred',
              'bisque', 'lightgreen', 'cyan', 'hotpink', 'gray', 'indianred', 'antiquewhite', 'royalblue', 'yellow',
              'indigo', 'lightcoral', 'darkslategrey', 'sienna', 'lightslategray', 'mediumblue', 'red', 'khaki',
              'darkviolet', 'mediumorchid', 'darkblue', 'lightskyblue', 'turquoise', 'lightyellow', 'grey',
              'whitesmoke', 'blueviolet', 'orchid', 'mediumslateblue', 'darkturquoise', 'coral', 'forestgreen',
              'gainsboro', 'darkorange', 'cornflowerblue', 'lightsteelblue', 'plum', 'lavender', 'palegreen',
              'darkred', 'dimgray', 'floralwhite', 'orangered', 'oldlace', 'darksalmon', 'lavenderblush',
              'darkslategray', 'tan', 'cadetblue', 'silver', 'tomato', 'darkkhaki', 'slategray', 'maroon', 'olive',
              'deeppink', 'linen', 'magenta', 'crimson', 'mistyrose', 'lime', 'saddlebrown', 'blanchedalmond', 'black',
              'snow', 'seashell', 'darkcyan', 'gold', 'midnightblue', 'darkgoldenrod', 'palevioletred', 'fuchsia',
              'teal', 'lightpink', 'darkgrey', 'mediumspringgreen', 'aquamarine', 'lightsalmon', 'navajowhite',
              'darkgreen', 'burlywood', 'rosybrown', 'springgreen', 'purple', 'olivedrab', 'lightslategrey', 'orange',
              'aliceblue', 'mediumaquamarine', 'navy', 'salmon', 'rebeccapurple', 'darkmagenta', 'limegreen',
              'deepskyblue', 'pink', 'mediumpurple', 'skyblue', 'aqua', 'blue', 'slategrey', 'darkslateblue',
              'honeydew', 'darkseagreen', 'paleturquoise', 'brown', 'thistle', 'lemonchiffon', 'peru', 'cornsilk',
              'papayawhip', 'green', 'lightgoldenrodyellow', 'mediumturquoise', 'steelblue', 'lightgray', 'lightgrey',
              'beige', 'palegoldenrod', 'darkgray', 'white', 'ghostwhite', 'dodgerblue', 'greenyellow', 'dimgrey',
              'darkorchid'}
    if inp.lower() in colors:
        return False
    elif inp[0] == "#" and len(inp) == 7:
        for i in range(1, len(inp)):
            if 0 < i and i > 16: #or ord(str(inp[i])) in range(97, 103):
                print(False)
        return True
    else:
        return False


def style_template(backcolor, headcolor, fontstyle, fontcolor):
    """
    The function is to make a copy of the template
    :param backcolor: background color
    :param headcolor: head font color
    :param fontstyle: font
    :param fontcolor: font color
    :return:
    """
    with open("style_template.txt") as fname:
        with open("index.html", "a") as file_out:
            for line in fname:
                if "@BACKCOLOR" in line:
                    file_out.write(line.replace("@BACKCOLOR", str(backcolor)))
                elif "@HEADCOLOR" in line:
                    file_out.write(line.replace("@HEADCOLOR", str(headcolor)))
                elif "@FONTSTYLE" in line:
                    file_out.write(line.replace("@FONTSTYLE", str(fontstyle)))
                elif "@FONTCOLOR" in line:
                    file_out.write(line.replace("@FONTCOLOR", str(fontcolor)))
                else:
                    file_out.write(line)


def font_check(inp):
    """
    verify the font
    :param inp: input of the font
    :return:
    """
    Fonts = {0: "Arial", 1: "Times New Roman", 2: "Comic Sans MS", 3: "Lucida Grande", 4: "Tahoma", 5: "Verdana",
             6: "Helvetica"}
    if inp in Fonts:
        return Fonts[inp]
    else:
        i = int(input("Please enter a valid option[0-6]: "))
        font_check(i)


def font_input(fontprompt):
    """
    The function is to check the input related to the pop-up window
    :param fontprompt: the promt
    :return:
    """
    if fontprompt == "yes" or "y":
        print("Close the Window once you have made the choice")
        turtle_dialog_box()
        print("Choose a font by its number \n 0. Arial \n 1.Times New Roman \n 2.Comic Sans MS \n 3. Lucida Grande \n "
              "4. Tahoma \n 5. Verdana \n 6. Helvetica ")
    elif fontprompt == "no" or "n":
        print("Choose a font by its number \n 0. Arial \n 1.Times New Roman \n 2.Comic Sans MS \n 3. Lucida Grande \n "
              "4. Tahoma \n 5. Verdana \n 6. Helvetica ")
    else:
        i = int(input("Enter a valid entry"))
        font_input(i)


def add_head1(heading,f):
    """
    write the heading 1
    :param heading: heading in text
    :param f: file
    :return:
    """
    f.write("<h1>" + heading + "</h1>")


def add_head2(heading2,f):
    """
    write the heading 2
    :param heading2: 2nd heading in text
    :param f: file
    :return:
    """
    f.write("<h2>" + heading2 + "</h2>")


def add_para(para,f):
    """
    the function adds the paragraph
    :param para: paragraph as text
    :param f: file
    :return:
    """
    f.write("<p>" + para + "</p>")


def add_img(img,f):
    """
    the function add the image
    :param img: image to be added
    :param f: file added to
    :return:
    """
    f.write("<img src='" + img + "'/>")


def website_mode(html_tags, filename):
    """
    the function reads the text files adds all the data to respective tags
    :param html_tags: the html tags
    :param filename: file with data
    :return: tags
    """
    tags = html_tags
    count = 0
    title = ""
    para = ""
    images = []
    with open(filename) as fname:
        title = fname.readline.strip('\n')  # adding the title to the tags
        for line in fname:
            line = line.strip('\n')
            if "!new_paragraph" in line:
                if "!title" in line:
                    title[count] = line.split(" ")
                    # adding all the lines in the para and images
                    while True:
                        if (line != ""):
                            line = fname.readline().strip('\n')
                        else:
                            break
                        while "!image" in line:
                            line = line.split(" ")
                            images.append(line[1])
                            line = fname.readline().strip('\n')
                        para.append(line.append('\n'))
                    images[html_tags.titles[count]] = images
                    paras[count] = para
                images = []
                para = ""
    return tags


def wizard_mode():
    """
    the function runs in the wizard mode using all the previous functions
    :return:
    """
    title = input("Please enter the title of the Web Page: ")
    print("Background Color")
    backcolor = input("Please enter a name of color, or in format '#xxxxxx': ")
    print("you will now choose a font.")
    fontprompt = input("Do you want to see the fonts first?")

    font_input(fontprompt)

    font_option = int(input())
    fontstyle = font_check(font_option)
    fontcolor = str(input("Please enter a color for the font: "))
    headcolor = str(input("Please enter a color for head: "))
    style_template(backcolor, headcolor, fontstyle, fontcolor)
    f = open("index.html", "a")
    f.write("<body>")
    heading = input("Enter heading")
    add_head1(heading, f)
    cont = 'y'
    while(cont=='y'):
        heading2 = input("Enter paragraph heading => ")
        add_head2(heading2, f)
        para = input("Enter paragraph => ")
        add_para(para,f)
        x = input("Do you want to add an image? ")
        if x == 'y' or x == 'yes':
            img = input("Enter image location => ")
            add_img(img, f)
        cont = input("Do you want to continue?'y'/'n'")
    print("your website is created as index.html")
    f.write("</body>")
    f.write("</html>")
    f.close()


def main():
    filename = fname
    if filename is None:
        wizard_mode()
    else:
        website_mode(html_tags, filename)


main()