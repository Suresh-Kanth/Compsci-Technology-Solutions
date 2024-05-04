# Compsci-Technology-Solutions

# Connected Frontend with Backend using Django
This project demonstrates how to connect a frontend interface with a backend server using Django.<br> Users can input details through a web page, submit them, and have the data stored in a database .<br>Additionally, the submitted data can be viewed in the Django admin interface.
## Installation
1. Clone this repository:
   ```
   git clone https://github.com/Suresh-Kanth/Compsci-technology.git
   ```
2. Navigate to the project directory:
   ```
   cd Compsci-technology/
   ```
3. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
## Usage
1. Start the Django development server:
   ```
   python manage.py runserver
   ```
2. Open a web browser and navigate to `http://127.0.0.1:8000/` to access the web page.
3. Enter the details in the web form and click "Submit" to save the data to the database.
4. To view the submitted data in the Django admin interface:
   - Open a web browser and navigate to `http://127.0.0.1:8000/admin/`.
   - Log in with the superuser credentials:
     - Username: admin
     - Password: admin
   - You should be able to see the models and the submitted data under the respective model.
