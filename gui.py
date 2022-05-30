import tkinter as tk
from tkinter.filedialog import askopenfile
import cv2
from PIL import ImageTk,Image


class Data:
    """
    Class to represent the form data for all the screens in the application.
    """

    def __init__(self):
        self.image_and_text_outputs = [None, None, None]
        self.image_file_path = ""
        self.image_text = ""

    def get_image_and_text_outputs(self):
        """
        Desc:
            getter method for the main list output for this class [isImage: bool, file_path:str,image_text: str]
        Inputs: N/A
        Return: N/A
        """
        return self.image_and_text_outputs

    def get_image_file_path(self):
        """
        Desc:
            getter method for images file path
        Inputs: N/A
        Return: N/A
        """

        return self.image_file_path

    def get_image_text(self):
        """
        Desc:
            getter method for images associated text
        Inputs: N/A
        Return:
            image_text: string value representing the text contained on an image.
        """
        return self.image_text

    def set_image_and_text_outputs(self,p1,p2,p3):
        """
        Desc:
            Method to set the list values in the form of [isImage: bool, file_path:str,image_text: str]
        Inputs:
            p1: bool value for whether we are comparing an image or just text
            p2: False for just text  or image path if comparing image
            p3: text either for the image or just the text.
        Return: N/A
        """
        self.image_and_text_outputs[0] = p1
        self.image_and_text_outputs[1] = p2
        self.image_and_text_outputs[2] = p3

    def set_image_file_path(self,file_path):
        """
        Desc:
            setter method to set the file_path for the image
        Inputs: N/A
        Return: N/A
        """
        self.image_file_path = file_path

    def set_image_text(self,image_text):
        """
        Desc:
            setter method to set the images printed text
        Inputs: N/A
        Return: N/A
        """
        self.image_text = image_text

def initialise_tkinter():
    return_dictionary = {}
    # create an instance of formData class
    formData = Data()
    return_dictionary['form_data'] = formData
    scaled_image_size = []

    root = tk.Tk()
    return_dictionary['root_window'] = root
    root.title("Trademark Checking Tool")
    root.geometry("500x500")

    # SETTING UP THE DIFFERENT SCREENS IN THE APPLICATION

    home_page = tk.Frame(root, width=500, height=500)
    return_dictionary['home_page_frame'] = home_page
    image_and_image_text = tk.Frame(root, width=500, height=500)
    return_dictionary['image_and_image_text_frame'] = image_and_image_text
    just_text = tk.Frame(root, width=500, height=500)
    return_dictionary['just_text_frame'] = just_text

    # set the initial frame of the application.
    home_page.pack(side=tk.TOP, anchor="w")

    # create the home_page of the application

    # HOME PAGE HEADING
    home_page_heading = tk.Label(home_page, text="Home Page of Trademark Application", font=('Helvatical bold', 16))
    home_page_heading.pack(side=tk.TOP, anchor="c", pady=(0, 5))
    return_dictionary['home_page_heading_label'] = home_page_heading

    # BUTTON TO TRANSITION TO THE IMAGE AND TEXT PAGE
    transition_to_image_and_text = tk.Button(home_page, text="Compare Image")
    transition_to_image_and_text.config(command=lambda:transition_between_frames(home_page,image_and_image_text))
    transition_to_image_and_text.pack(side=tk.TOP, anchor="c", pady=(0, 5), padx=5, fill="x")
    return_dictionary['transition_btn_home_to_image_and_text'] = transition_to_image_and_text

    # BUTTON TO TRANSITION TO THE TEXT ONLY PAGE
    transition_to_text = tk.Button(home_page, text="Compare Text")
    transition_to_text.config(command=lambda:transition_between_frames(home_page,just_text))
    transition_to_text.pack(side=tk.TOP, anchor="c", pady=(0, 5), padx=5, fill="x")
    return_dictionary['transition_btn_home_to_text'] = transition_to_text

    # first part of the interface label for choose your image.
    open_image_text_label = tk.Label(image_and_image_text, text="Choose your image", font=('Helvatical bold', 16))
    open_image_text_label.pack(side=tk.TOP, anchor="w", pady=(0, 5))
    return_dictionary['choose_image_text_label'] = open_image_text_label

    # second part of interface tell the user the file format.

    imageText = tk.Label(image_and_image_text, text='Upload image with extension png or jpg',font=('Helvatical bold', 14))
    imageText.pack(side=tk.TOP, anchor="w", padx=10, pady=(0, 5))
    return_dictionary['image_format_text_label'] = imageText

    # third part is a button to upload the image file opens the file explorer.

    uploadButton = tk.Button(image_and_image_text, text='Upload File', command=lambda:open_file(formData,canvas,scaled_image_size))
    uploadButton.pack(side=tk.TOP, anchor="w", padx=10, pady=(0, 5))
    return_dictionary['upload_image_btn'] = uploadButton

    # create a label
    # first part of the interface label for choose your image.
    enter_image_text_label = tk.Label(image_and_image_text, text="Enter Image text", font=('Helvatical bold', 16))
    enter_image_text_label.pack(side=tk.TOP, anchor="w", pady=(0, 5))
    return_dictionary['enter_image_text_label'] = enter_image_text_label

    # create the text box for the user to enter the image text.
    text_box = tk.Text(image_and_image_text, height=1, width=40)
    text_box.pack(side=tk.TOP, anchor="w", padx=10, pady=(0, 5))
    return_dictionary['enter_image_textbox'] = text_box

    # submit text button
    get_text_button = tk.Button(image_and_image_text, text='Submit Image Text', command=lambda:get_textbox_text(text_box,formData,text_label))
    get_text_button.pack(side=tk.TOP, anchor="w", padx=10, pady=(0, 5))
    return_dictionary['submit_text_btn'] = get_text_button

    # submit both image and text for processing
    send_image_and_text_for_processing_btn = tk.Button(image_and_image_text, text="Send Image and Text for Processing")
    send_image_and_text_for_processing_btn.config(command=lambda: getInput(return_dictionary))
    send_image_and_text_for_processing_btn.pack(side=tk.TOP, anchor="w", padx=5, pady=(0, 5))
    return_dictionary['submit_text_and_image_btn'] = send_image_and_text_for_processing_btn

    # heading for displaying the chosen image
    uploaded_image_label = tk.Label(image_and_image_text, text="Current Uploaded image", font=('Helvatical bold', 16))
    uploaded_image_label.pack(side=tk.TOP, anchor="w", pady=(0, 5))
    return_dictionary['heading_display_chosen_image_label'] = uploaded_image_label

    # create the canvas for our image that has been uploaded.
    canvas = tk.Canvas(image_and_image_text, width=100, height=100)
    canvas.pack(side=tk.TOP, anchor="w", padx=10, pady=(0, 5))
    return_dictionary['preview_image_canvas'] = canvas

    uploaded_image_text_label = tk.Label(image_and_image_text, text="Current uploaded image text",font=('Helvatical bold', 16))
    uploaded_image_text_label.pack(side=tk.TOP, anchor="w", pady=(0, 5))
    return_dictionary['upload_image_text_label'] = uploaded_image_text_label


    text_label = tk.Label(image_and_image_text, text="", font=('Helvatical bold', 14))
    text_label.pack(side=tk.TOP, anchor="w", padx=10, pady=(0, 5))
    return_dictionary['preview_image_text_label'] = text_label

    btn_image_and_text_to_home = tk.Button(image_and_image_text, text="Back to home page")
    btn_image_and_text_to_home.config(command=lambda:transition_between_frames(image_and_image_text,home_page))
    btn_image_and_text_to_home.pack(side=tk.TOP, anchor="w", padx=10, pady=(0, 5))

    return_dictionary['transition_btn_text_to_home'] = btn_image_and_text_to_home
    # JUST TEXT COMPARISON


    root.mainloop()
    return return_dictionary


# FUNCTIONS TO CALL TO TRANSITION BETWEEN PAGES
def transition_between_frames(current_frame, destination_frame):
    """
    Desc:
        Function to transition the frame of the interface from the home frame, to the image_and_text frame
    Inputs: N/A
    Returns: N/A
    """
    current_frame.pack_forget()
    destination_frame.pack(side= tk.TOP, anchor="w")

# IMAGE AND IMAGE TEXT INTERFACE ITEMS AND FUNCTIONS
def resize_image(path,sf,scaled_image_size):
    """
    Desc:
        This function rescales the image according to the scaling factor
    Inputs:
        path: string path to the original image to be resized
        sf: integer value between 1-100, will determine what size you want the image to be scaled to
    Returns:
        returns a numpy Array of the resized image.
    """
    src = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

    # percent by which the image is resized
    scale_percent = sf

    # calculate the scaled percent percent of original dimensions
    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)

    # dsize
    dsize = (width, height)

    for width_height in list(dsize):
        scaled_image_size.append(width_height)

    # resize image
    output = cv2.resize(src, dsize)
    return output


def open_file(formData,canvas,scaled_image_size):
    """
    Desc:
        This function is responsible for opening an image file either jpg, or png.
    Inputs: N/A
    Returns: N/A
    """
    file_path = askopenfile(mode='r', filetypes=[('Image Files', 'jpg'),('Image Files', 'png')])
    if file_path is not None:
        formData.set_image_file_path(file_path.name)
        # resize the image to 10% of its original size
        resize_image(file_path.name,10,scaled_image_size)
        # display the resized image as the uploaded image.
        display_image_and_text(file_path.name,canvas,scaled_image_size)

def get_textbox_text(text_box,formData,text_label):
    """
    Desc:
        this function is responsible for retrieving the text from the image, from the textbox.
        It also deletes the submitted text for a clean textbox for next time.
    Inputs: N/A
    Returns: N/A
    """

    image_text = text_box.get("1.0",tk.END)
    display_text(formData,image_text,text_label)
    text_box.delete("1.0", tk.END)

def getInput(dictionary):
    """
    Desc:
        this function passes the input in the form of [True, file_path, image_text] if the data is coming from the image_and_image_text screen.
        and passes the input in the form of [False,False, text] if it coming just from the text screen of the application.
    Inputs:
        button: The button instance that is being clicked to submit the form data.
    Returns:
        the list in the form of [True, file_path, image_text] if its coming from the image_and_image_text frame or
        the list in the form of [False, False, text] if its coming from the just_text screen.
    """
    button = dictionary.get('submit_text_and_image_btn')
    image_and_image_text_frame = dictionary.get('image_and_image_text_frame')
    just_text_frame = dictionary.get('just_text_frame')
    form_data = dictionary.get('form_data')
    if button.master == image_and_image_text_frame:
        form_data.set_image_and_text_outputs(True,form_data.get_image_file_path(),form_data.get_image_text())
    elif button.master == just_text_frame:
        form_data.set_image_and_text_outputs(False, False, form_data.get_image_text())

    print(form_data.get_image_and_text_outputs())
    return form_data.get_image_and_text_outputs()


def display_text(formData,image_text,text_label):
    """
    Desc:
        this function displays the text to the screen showing the user the image text that they entered
    Inputs:
        image_text: a string representing the images text.
    Returns: N/A
    """
    # current uploaded image text
    text_label.config(text=image_text)
    formData.set_image_text(image_text.strip("\n"))


def display_image_and_text(file_path, canvas, scaled_image_size):
    """
    Desc:
        this function updates the canvas with a preview of the newly uploaded image.
    Inputs:
        file_path: a string representing the path to the image file.
    Returns: N/A
    """
    # create the image size dynamically based on what the image scaling resizes the image to
    canvas.config(width=scaled_image_size[0],height=scaled_image_size[1])
    # get the numpy array of the resized image
    resized_image = Image.fromarray(resize_image(file_path, 10,scaled_image_size))

    ph = ImageTk.PhotoImage(resized_image)

    canvas.image = ph  # to prevent the image garbage collected.
    canvas.create_image((0, 0), image=ph, anchor='nw')


initialise_tkinter()