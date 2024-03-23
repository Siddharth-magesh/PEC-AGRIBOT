import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, QLineEdit, QGroupBox 
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import weather_pred as wp
import dynamic_data_updation as ddu
import pesticide_management as pm
import image_analyzation as ia
import speech as sp

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 600, 800)

        self.initUI()

    def initUI(self):
        # Create layout
        layout = QVBoxLayout()
        
        # Create label for the image
        # Load image
        image_label = QLabel(self)
        pixmap = QPixmap("D:\workspace\codespace\pec\logo.png")  # Path to your image file
        scaled_pixmap = pixmap.scaled(100, 100, aspectRatioMode=Qt.KeepAspectRatio)  # Adjust the size as needed
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)  # Align image to the top and horizontally centered
        layout.addWidget(image_label)
        
        # Create label for the text below the image
        text_label = QLabel("Bringing agriculture to your fingertips\nwith Agri Bot - \nyour virtual farming companion!", self)
        text_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)  # Align text to the top and horizontally centered
        font = QFont()
        font.setBold(True)  # Make the text bold
        font.setPointSize(12)  # Set font size to 12
        text_label.setFont(font)
        layout.addWidget(text_label)

        # Create layout for buttons
        button_layout = QHBoxLayout()

        # Styling the buttons
        button_style = """
        QPushButton {
            background-color: #f0f0f0; /* Light gray background */
            border: 2px solid #555555; /* Dark gray border */
            color: #333333; /* Dark gray text */
            padding: 10px 20px; /* Padding for better appearance */
            font-size: 16px; /* Font size */
            font-weight: bold; /* Bold font */
        }
        
        QPushButton:hover {
            background-color: #d3d3d3; /* Lighter gray background on hover */
        }
        """

        # Apply the style to each button
        self.page1_button = QPushButton('Help-Desk', self)
        self.page1_button.clicked.connect(self.showPage1)
        self.page1_button.setStyleSheet(button_style)
        button_layout.addWidget(self.page1_button)
        
        self.page2_button = QPushButton('budget management', self)
        self.page2_button.clicked.connect(self.showPage2)
        self.page2_button.setStyleSheet(button_style)
        button_layout.addWidget(self.page2_button)
        
        self.page3_button = QPushButton('crop evaluation', self)
        self.page3_button.clicked.connect(self.showPage3)
        self.page3_button.setStyleSheet(button_style)
        button_layout.addWidget(self.page3_button)
        
        layout.addLayout(button_layout)
        
        # Create a placeholder for the current page
        self.current_page = None
        
        self.setLayout(layout)

    def showPage1(self):
        self.clearLayout()
        self.current_page = DatabaseUpdater()
        self.layout().addWidget(self.current_page)

    def showPage2(self):
        self.clearLayout()
        self.current_page = MobileWindow()
        self.layout().addWidget(self.current_page)

    def showPage3(self):
        self.clearLayout()
        self.current_page = ImageSelector()
        self.layout().addWidget(self.current_page)

    def clearLayout(self):
        if self.current_page:
            self.current_page.deleteLater()

class DatabaseUpdater(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Database Updater")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Horizontal layout for buttons and input box
        button_layout = QHBoxLayout()

        # Update Database Button
        self.update_database_button = QPushButton('Update Database', self)
        self.update_database_button.clicked.connect(self.updateDatabaseClicked)
        self.update_database_button.setStyleSheet("font-weight: bold; font-size: 16px; padding: 10px;")
        button_layout.addWidget(self.update_database_button)

        # Vertical layout for input box and submit button
        input_layout = QVBoxLayout()

        # Input Box
        self.input_box = QLineEdit(self)
        input_layout.addWidget(self.input_box)

        # Submit Button
        self.submit_button = QPushButton('Get Climate', self)

        self.submit_button.clicked.connect(self.submitClicked)
        input_layout.addWidget(self.submit_button)

        button_layout.addLayout(input_layout)

        layout.addLayout(button_layout)

        # Output Label
        self.output_label = QLabel(self)
        self.output_label.setAlignment(Qt.AlignCenter)
        self.output_label.setStyleSheet("border: 2px solid black; background-color: #f0f0f0; padding: 10px;")
        layout.addWidget(self.output_label)

        # Talk Button
        self.talk_button = QPushButton('Talk', self)
        self.talk_button.clicked.connect(self.talkClicked)
        self.talk_button.setFixedSize(100, 100)
        self.talk_button.setStyleSheet("border-radius: 50px; background-color: #555555; color: white; font-weight: bold;")
        layout.addWidget(self.talk_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def submitClicked(self):
        # Get input text from input box
        input_text = self.input_box.text()

        result1 = wp.load_temp(input_text)
        
        self.output_label.setText(str(result1))

    def updateDatabaseClicked(self):
        result2 = ddu.process_sentences('article1.txt')
        self.output_label.setText(str(result2))

    def talkClicked(self):
        user_input = sp.listen()
        if "hello" in user_input:
            output = "Hello! How are you?"
        elif "how are you" in user_input:
            output = "I am fine, what about you?"
        elif "thank you" in user_input:
            output = "You're welcome! If you have any more questions \nor need further assistance, feel free to ask. Have a great day!"
        elif "services" in user_input:
            output = "We offer a variety of services including crop \nmanagement. Is there something specific you're interested in?"
        elif "hi" in user_input:
            output = "Hi there! How are you?"
        elif "hey" in user_input:
            output = "Hey! How can I help you optimize your crop \nmanagement practices?"
        elif "morning" in user_input:
            output = "Good morning! Are you looking for information\n or assistance with your crops today?"
        elif "question" in user_input:
            output = "Hi! I'm here to help. What's your question \nregarding crop management?"
        elif "thanks" in user_input:
            output =  "You're welcome! If you have any more \nquestions in the future, don't hesitate to reach out."
        elif "improve soil fertility" in user_input:
            output = "To improve soil fertility, you can \nincorporate organic matter like compost or manure, practice crop rotation, and conduct soil tests\n to determine nutrient deficiencies. Adjusting pH levels and applying balanced\n fertilizers can also help replenish nutrients."
        elif "control weeds" in user_input:
            output = "You can control weeds through various \nmethods such as mulching, hand weeding, using mechanical tools like cultivators, and applying\n herbicides selectively. Implementing integrated weed management strategies can\n help minimize weed pressure while protecting your crops."
        elif "maximize crop yields" in user_input:
            output = "To maximize crop yields, focus on optimizing \ngrowing conditions by maintaining soil fertility, managing pests and diseases effectively,\n selecting high-yielding crop varieties suited to your region, and practicing\n proper planting and harvesting techniques."
        elif "identify nutrient deficiencies" in user_input:
            output = "You can identify nutrient deficiencies by \nobserving symptoms such as yellowing or stunted growth in plants. Conducting soil tests and\n leaf analysis can also help pinpoint specific nutrient deficiencies, allowing\n you to address them through targeted fertilization."
        elif "common diseases" in user_input:
            output = "Common crop diseases include fungal,\n bacterial, and viral infections. To prevent them, practice crop rotation, use disease-resistant\n varieties, maintain proper sanitation, and avoid overwatering. Timely detection\n and treatment with appropriate fungicides or other remedies can also help manage\n diseases effectively."
        elif "deal with soil erosion" in user_input:
            output = "Implement practices like contour plowing, \nterracing, and planting cover crops to prevent soil erosion."
        elif "organic or synthetic fertilizers" in user_input:
            output = "Both have their advantages. Organic \nfertilizers improve soil structure and microbial activity, while synthetic fertilizers provide\n immediate nutrient availability."
        else:
            output = "I'm sorry, I didn't understand that. \nCould you please repeat?"
        sp.talk(output)
        self.output_label.setText(output)
class MobileWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mobile Window")
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        
        fertilizer_groupbox = QGroupBox("Fertilizer Prediction")
        fertilizer_layout = QVBoxLayout()

        # Create input boxes for fertilizer prediction
        self.crop_input = QLineEdit(self)
        self.crop_input.setPlaceholderText('Enter crop')
        fertilizer_layout.addWidget(self.crop_input)

        self.acreage_input = QLineEdit(self)
        self.acreage_input.setPlaceholderText('Enter acreage')
        fertilizer_layout.addWidget(self.acreage_input)

        self.purpose_input = QLineEdit(self)
        self.purpose_input.setPlaceholderText('Enter purpose')
        fertilizer_layout.addWidget(self.purpose_input)

        # Create submit button for fertilizer prediction
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setStyleSheet("background-color: lightgreen;")
        self.submit_button.clicked.connect(self.submit)
        fertilizer_layout.addWidget(self.submit_button)

        fertilizer_groupbox.setLayout(fertilizer_layout)
        main_layout.addWidget(fertilizer_groupbox)

        crop_price_groupbox = QGroupBox("Crop Price Prediction")
        crop_price_layout = QVBoxLayout()

        # Create input box for crop name
        self.crop_name_input = QLineEdit(self)
        self.crop_name_input.setPlaceholderText('Enter crop name')
        crop_price_layout.addWidget(self.crop_name_input)

        # Create submit button for crop price prediction
        self.submit_button_2 = QPushButton('Submit Crop', self)
        self.submit_button_2.setStyleSheet("background-color: lightgreen;")
        self.submit_button_2.clicked.connect(self.submit_crop)
        crop_price_layout.addWidget(self.submit_button_2)

        crop_price_groupbox.setLayout(crop_price_layout)
        main_layout.addWidget(crop_price_groupbox)
        # Create output box
        self.output_box = QLabel(self)
        self.output_box.setStyleSheet("background-color: #cccccc; border: 1px solid #ccc; font-size: 14px;")
        main_layout.addWidget(self.output_box)

        self.setLayout(main_layout)
        self.show()

    def submit(self):
        # Get values from input boxes for fertilizer prediction
        crop = self.crop_input.text()
        acreage = int(self.acreage_input.text())
        pesticide_type = self.purpose_input.text()
        
        result = pm.apply_pesticide(crop, acreage, pesticide_type)
        pest_name, pest_brand, price_per_acre, price_per_gallon = result
        message = f"<span style='color: blue;'>Fertilizer Prediction</span><br>Pesticide: {pest_name}<br>Brand: {pest_brand}<br>Total price: {price_per_acre}<br>Total number of Gallons: {price_per_gallon}"
        self.output_box.setText(message)

    def submit_crop(self):
        # Get crop name from input box for crop price prediction
        crop_name = self.crop_name_input.text()
        result1 = pm.get_prices(crop_name)
        crop_price , seed_price = result1
        message = f"<span style='color: red;'>Crop Price Prediction</span><br>Crop Name: {crop_name}<br>Crop price: {crop_price}<br>Seed price : {seed_price}"
        self.output_box.setText(message)

class ImageSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Selector")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Set window size and title
        self.setGeometry(100, 100, 680, 800)
        self.setWindowTitle('Image Selector')

        # Create layout
        layout = QVBoxLayout()

        # Create buttons layout
        button_layout = QHBoxLayout()

        # Create buttons to select images
        self.button_1 = QPushButton('Select Image 1', self)
        self.button_1.clicked.connect(self.selectImage1)
        button_layout.addWidget(self.button_1)

        self.button_2 = QPushButton('Select Image 2', self)
        self.button_2.clicked.connect(self.selectImage2)
        button_layout.addWidget(self.button_2)

        layout.addLayout(button_layout)

        # Create image labels
        self.image_label_1 = QLabel(self)
        layout.addWidget(self.image_label_1)

        self.image_label_2 = QLabel(self)
        layout.addWidget(self.image_label_2)

        # Create submit button
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.submitImages)
        layout.addWidget(self.submit_button)

        # Create label to display result
        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.show()

    def selectImage1(self):
        self.image_path_1, _ = QFileDialog.getOpenFileName(self, 'Select Image 1', '', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
        if self.image_path_1:
            pixmap = QPixmap(self.image_path_1)
            self.image_label_1.setPixmap(pixmap)
            self.image_label_1.setScaledContents(True)

    def selectImage2(self):
        self.image_path_2, _ = QFileDialog.getOpenFileName(self, 'Select Image 2', '', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
        if self.image_path_2:
            pixmap = QPixmap(self.image_path_2)
            self.image_label_2.setPixmap(pixmap)
            self.image_label_2.setScaledContents(True)

    def submitImages(self):
        if self.image_path_1 and self.image_path_2:
            targetted_class = ia.classify_vegetable(self.image_path_1)
            targetted_class_condition = ia.vegetable_condition_check(targetted_class, self.image_path_2)
            result_text = f"Predicted product : {targetted_class}\n product condition : {targetted_class_condition}"
            self.result_label.setText(result_text)
        else:
            self.result_label.setText("Please select both images.")
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


