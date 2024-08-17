
# PII Detection and Masking Tool

This system is a PII (Personally Identifiable Information) detection and masking tool designed to identify and protect sensitive information within text data. Built using a machine learning model, the system scans for common types of PII, such as names, emails, phone numbers, and addresses, and replaces them with placeholder tags. This ensures that the text can be safely shared or processed without exposing private details. The system is easy to use and can handle a variety of text formats, making it an essential tool for enhancing data privacy and security in digital communications.

## How to Use This Project

1. **Download or Clone the Repository:**

   You can either download or clone this repository to your local machine.

2. **Install the Required Libraries:**

   Install the dependencies listed in the `requirements.txt` file using the following command:

   ```bash
   pip install -r requirements.txt
   ```

3. **Open the Project in VSCode:**

   Open the project in Visual Studio Code (VSCode).

4. **Start the Flask Server:**

   Start the Flask server by running the appropriate script.

5. **Access the Application in a Web Browser:**

   Open your web browser and go to the following URL:

   ```text
   http://127.0.0.1:5000/
   ```

6. **Upload a File:**

   You can choose a file and upload it through the web interface. The file will be processed within seconds, and you will be redirected to the results page where you will see the original text alongside the PII-detected text.

### Additional Information

- **File Storage:** Uploaded files will be saved inside the `uploads` folder in the system files.

- **PII Detection:** The detected PII information will be replaced with `[PII]` in red color. You can change the color in the `style.css` file located in the `static` folder. If you want to change the placeholder text, you can modify it in the `app.py` file.

## Dependencies

This application uses the following libraries, which should be installed before running the application (they are listed in the `requirements.txt` file):

- Flask
- Joblib
- Werkzeug

## Responsive Design

![Screenshot 2024-08-17 142712](https://github.com/user-attachments/assets/59b78097-629f-4d80-a8f1-4e96b2b28c7a)

![Screenshot 2024-08-17 142725](https://github.com/user-attachments/assets/24311c94-000c-4d05-b6ba-a647a65be746)