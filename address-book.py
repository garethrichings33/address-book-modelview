from MainWindow import Ui_MainWindow
from ContactWindow import Ui_ContactWindow
from PySide6.QtWidgets import QPushButton, QMainWindow, QApplication, QMessageBox
from PySide6.QtCore import QAbstractListModel, QModelIndex, QPersistentModelIndex, Qt
import sys
import json

if __name__ == "__main__":

    class MainWindow(QMainWindow, Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)

            self.model = ContactsModel()
            self.load()
            self.contactList.setModel(self.model)

            self.connect_buttons()

            self.contactList.clicked.connect(self.activate_delete_contact)
            self.contactList.clicked.connect(self.activate_view_contact)

        def connect_buttons(self):
            self.addContactButton.pressed.connect(self.add_contact)
            self.deleteContactButton.pressed.connect(lambda:
                                                     self.confirm_delete_contact(self.contactList.currentIndex().row()))
            self.viewContactButton.pressed.connect(lambda:
                                                   self.view_contact(self.contactList.currentIndex().row()))

        def activate_delete_contact(self):
            self.deleteContactButton.setEnabled(True)

        def activate_view_contact(self):
            self.viewContactButton.setEnabled(True)

        def add_contact(self):
            self.add_contact_window = AddContactWindow(self, self.model)
            self.setEnabled(False)

        def confirm_delete_contact(self, index):
            contact = self.model.contacts[index].get('id')
            dialog = QMessageBox(self)
            dialog.setWindowTitle("Delete?")
            dialog.setIcon(QMessageBox.Question)
            dialog.setText("Really delete contact " + contact + "?")
            dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            button = dialog.exec()
            if button == QMessageBox.Ok:
                self.delete_contact(index)
            elif button == QMessageBox.Cancel:
                self.deleteContactButton.setDown(False)

        def delete_contact(self, contact_id):
            self.model.contacts.pop(contact_id)
            self.save()
            self.deleteContactButton.setEnabled(False)
            self.viewContactButton.setEnabled(False)
            self.model.layoutChanged.emit()

        def view_contact(self, contact_id):
            self.view_contact_window = ViewContactWindow(
                self, self.model, contact_id)
            self.setEnabled(False)
            self.view_contact_window.show()

        def load(self):
            try:
                with open('data.json', 'r') as f:
                    self.model.contacts = sorted(
                        json.load(f), key=lambda d: d['id'])
            except Exception as ex:
                print(ex)

        def save(self):
            with open('data.json', 'w') as f:
                json.dump(self.model.contacts, f)

    class ContactsModel(QAbstractListModel):
        def __init__(self, *args, contacts=None, **kwargs):
            super(ContactsModel, self).__init__(*args, **kwargs)
            self.contacts = contacts or []

        def data(self, index, role):
            if role == Qt.DisplayRole:
                contact = self.contacts[index.row()]
                if 'id' in contact:
                    return contact['id']

        def rowCount(self, index):
            return len(self.contacts)

    class ViewContactWindow(QMainWindow, Ui_ContactWindow):
        def __init__(self, main_window, model, contact_index):
            super().__init__()
            self.setupUi(self)

            self.main_window = main_window
            self.model = model
            self.contact_index = contact_index

            self.extract_contact_details()
            self.populate_forms()

            self.createButtons()
            self.positionButtons()

            self.contact_saved = True
            self.contact_altered = False

            self.connect_forms()
            self.connect_buttons()

            self.show()

        def createButtons(self):
            self.editContactButton = QPushButton()
            self.editContactButton.setFixedSize(100, 30)
            self.editContactButton.setText("Edit")

            self.saveContactButton = QPushButton()
            self.saveContactButton.setFixedSize(100, 30)
            self.saveContactButton.setText("Save")
            self.saveContactButton.setEnabled(False)

            self.closeButton = QPushButton()
            self.closeButton.setFixedSize(100, 30)
            self.closeButton.setText("Close")

        def positionButtons(self):
            self.horizontalLayout_2.addWidget(self.editContactButton)
            self.horizontalLayout_2.addWidget(self.saveContactButton)
            self.horizontalLayout_2.addWidget(self.closeButton)

        def extract_contact_details(self):
            self.contact = self.model.contacts[self.contact_index]
            self.first_name = self.contact['first_name']
            self.last_name = self.contact['last_name']
            self.house = self.contact['house']
            self.street = self.contact['street']
            self.town = self.contact['town']
            self.postcode = self.contact['postcode']
            self.phone = self.contact['phone']
            self.email = self.contact['email']
            self.contact_id = self.contact['id']

        def populate_forms(self):
            self.firstNameEdit.setText(self.first_name)
            self.lastNameEdit.setText(self.last_name)
            self.houseEdit.setText(self.house)
            self.streetEdit.setText(self.street)
            self.townEdit.setText(self.town)
            self.postcodeEdit.setText(self.postcode)
            self.phoneEdit.setText(self.phone)
            self.emailEdit.setText(self.email)
            self.contactIdEdit.setText(self.contact_id)

        def makeEditable(self):
            self.firstNameEdit.setEnabled(True)
            self.lastNameEdit.setEnabled(True)
            self.houseEdit.setEnabled(True)
            self.streetEdit.setEnabled(True)
            self.townEdit.setEnabled(True)
            self.postcodeEdit.setEnabled(True)
            self.phoneEdit.setEnabled(True)
            self.emailEdit.setEnabled(True)
            self.contactIdEdit.setEnabled(True)

            self.editContactButton.setEnabled(False)

        def makeUnEditable(self):
            self.firstNameEdit.setEnabled(False)
            self.lastNameEdit.setEnabled(False)
            self.houseEdit.setEnabled(False)
            self.streetEdit.setEnabled(False)
            self.townEdit.setEnabled(False)
            self.postcodeEdit.setEnabled(False)
            self.phoneEdit.setEnabled(False)
            self.emailEdit.setEnabled(False)
            self.contactIdEdit.setEnabled(False)

            self.editContactButton.setEnabled(True)

        def connect_forms(self):
            self.firstNameEdit.textChanged.connect(self.contact_edited)
            self.firstNameEdit.textChanged.connect(self.update_first_name)

            self.lastNameEdit.textChanged.connect(self.contact_edited)
            self.lastNameEdit.textChanged.connect(self.update_last_name)

            self.houseEdit.textChanged.connect(self.contact_edited)
            self.houseEdit.textChanged.connect(self.update_house)

            self.streetEdit.textChanged.connect(self.contact_edited)
            self.streetEdit.textChanged.connect(self.update_street)

            self.townEdit.textChanged.connect(self.contact_edited)
            self.townEdit.textChanged.connect(self.update_town)

            self.postcodeEdit.textChanged.connect(self.contact_edited)
            self.postcodeEdit.textChanged.connect(self.update_postcode)

            self.phoneEdit.textChanged.connect(self.contact_edited)
            self.phoneEdit.textChanged.connect(self.update_phone)

            self.emailEdit.textChanged.connect(self.contact_edited)
            self.emailEdit.textChanged.connect(self.update_email)

            self.contactIdEdit.textChanged.connect(self.contact_edited)
            self.contactIdEdit.textChanged.connect(self.update_contact_id)

        def connect_buttons(self):
            self.editContactButton.pressed.connect(self.makeEditable)
            self.saveContactButton.pressed.connect(self.save_contact)
            self.closeButton.pressed.connect(self.close_contact)

        def update_first_name(self, text):
            self.first_name = text

        def update_last_name(self, text):
            self.last_name = text

        def update_house(self, text):
            self.house = text

        def update_street(self, text):
            self.street = text

        def update_town(self, text):
            self.town = text

        def update_postcode(self, text):
            self.postcode = text

        def update_phone(self, text):
            self.phone = text

        def update_email(self, text):
            self.email = text

        def update_contact_id(self, text):
            self.contact_id = text

        def first_name_contact_id(self, text):
            self.contactIdEdit.setText(text)

        def contact_edited(self):
            self.contact_altered = True
            self.contact_saved = False
            self.editContactButton.setEnabled(False)
            self.saveContactButton.setEnabled(True)

        def save_contact(self):
            self.update_contact()

            if self.contact['id']:
                self.contact_saved = True
                self.contact_altered = False
                self.saveContactButton.setEnabled(False)
                self.makeUnEditable()
            else:
                self.no_contact_id_message()

            self.saveContactButton.setDown(False)

        def update_contact(self):
            self.contact['first_name'] = self.first_name
            self.contact['last_name'] = self.last_name
            self.contact['house'] = self.house
            self.contact['street'] = self.street
            self.contact['town'] = self.town
            self.contact['postcode'] = self.postcode
            self.contact['phone'] = self.phone
            self.contact['email'] = self.email
            self.contact['id'] = self.contact_id

        def save_contact_error(self, ex):
            dialog = QtWidgets.QMessageBox()
            dialog.setWindowTitle("Error Saving Contact")
            dialog.setText(str(ex))
            dialog.exec()

        def close_contact(self):
            if self.contact_altered and not self.contact_saved:
                self.contact_not_saved_warning()
            else:
                self.model.contacts = sorted(
                    self.model.contacts, key=lambda d: d['id'])
                self.model.layoutChanged.emit()
                self.main_window.save()
                self.close()
                self.main_window.setEnabled(True)

        def contact_not_saved_warning(self):
            dialog = QMessageBox(self)
            dialog.setWindowTitle("Contact Not Saved")
            dialog.setIcon(QMessageBox.Question)
            dialog.setText("Really close contact without saving?")
            dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            button = dialog.exec()
            if button == QMessageBox.Ok:
                self.close()
                self.main_window.setEnabled(True)
            elif button == QMessageBox.Cancel:
                self.closeButton.setDown(False)

    class AddContactWindow(QMainWindow, Ui_ContactWindow):
        def __init__(self, main_window, model):
            super().__init__()
            self.setupUi(self)

            self.main_window = main_window
            self.model = model

            self.createButton()
            self.positionButton()
            self.connectButton()

            self.init_variables()
            self.init_forms()

            self.connectForms()
            self.connect_first_name_id()

            self.show()

        def init_forms(self):
            self.clear_forms()
            self.enable_forms()

        def clear_forms(self):
            self.firstNameEdit.clear()
            self.lastNameEdit.clear()
            self.houseEdit.clear()
            self.streetEdit.clear()
            self.townEdit.clear()
            self.postcodeEdit.clear()
            self.phoneEdit.clear()
            self.emailEdit.clear()
            self.contactIdEdit.clear()

        def enable_forms(self):
            self.firstNameEdit.setEnabled(True)
            self.lastNameEdit.setEnabled(True)
            self.houseEdit.setEnabled(True)
            self.streetEdit.setEnabled(True)
            self.townEdit.setEnabled(True)
            self.postcodeEdit.setEnabled(True)
            self.phoneEdit.setEnabled(True)
            self.emailEdit.setEnabled(True)
            self.contactIdEdit.setEnabled(True)

        def init_variables(self):
            self.first_name = ""
            self.last_name = ""
            self.house = ""
            self.street = ""
            self.town = ""
            self.postcode = ""
            self.phone = ""
            self.email = ""
            self.contact_id = ""

        def createButton(self):
            self.addContactButton = QPushButton()
            self.addContactButton.setFixedSize(100, 30)
            self.addContactButton.setText("Add")
            self.addContactButton.setEnabled(False)

        def positionButton(self):
            self.horizontalLayout_2.addWidget(self.addContactButton)

        def connectButton(self):
            self.addContactButton.pressed.connect(self.save_new_contact)

        def connectForms(self):
            self.firstNameEdit.textChanged.connect(self.contact_edited)
            self.firstNameEdit.textChanged.connect(self.update_first_name)

            self.lastNameEdit.textChanged.connect(self.contact_edited)
            self.lastNameEdit.textChanged.connect(self.update_last_name)

            self.houseEdit.textChanged.connect(self.contact_edited)
            self.houseEdit.textChanged.connect(self.update_house)

            self.streetEdit.textChanged.connect(self.contact_edited)
            self.streetEdit.textChanged.connect(self.update_street)

            self.townEdit.textChanged.connect(self.contact_edited)
            self.townEdit.textChanged.connect(self.update_town)

            self.postcodeEdit.textChanged.connect(self.contact_edited)
            self.postcodeEdit.textChanged.connect(self.update_postcode)

            self.phoneEdit.textChanged.connect(self.contact_edited)
            self.phoneEdit.textChanged.connect(self.update_phone)

            self.emailEdit.textChanged.connect(self.contact_edited)
            self.emailEdit.textChanged.connect(self.update_email)

            self.contactIdEdit.textChanged.connect(self.contact_edited)
            self.contactIdEdit.textChanged.connect(self.update_contact_id)

        def connect_first_name_id(self):
            self.firstNameEdit.textChanged.connect(self.first_name_contact_id)

        def update_first_name(self, text):
            self.first_name = text

        def update_last_name(self, text):
            self.last_name = text

        def update_house(self, text):
            self.house = text

        def update_street(self, text):
            self.street = text

        def update_town(self, text):
            self.town = text

        def update_postcode(self, text):
            self.postcode = text

        def update_phone(self, text):
            self.phone = text

        def update_email(self, text):
            self.email = text

        def update_contact_id(self, text):
            self.contact_id = text

        def first_name_contact_id(self, text):
            self.contactIdEdit.setText(text)

        def contact_edited(self):
            self.addContactButton.setEnabled(True)

        def save_new_contact(self):
            contact = {'first_name': self.first_name,
                       'last_name': self.last_name,
                       'house': self.house,
                       'street': self.street,
                       'town': self.town,
                       'postcode': self.postcode,
                       'phone': self.phone,
                       'email': self.email,
                       'id': self.contact_id,
                       }

            if contact['id']:
                self.model.contacts.append(contact)
                self.main_window.save()

                self.model.contacts = sorted(
                    self.model.contacts, key=lambda d: d['id'])
                self.model.layoutChanged.emit()

                self.close()
                self.main_window.setEnabled(True)
            else:
                self.no_contact_id_message()

        def add_contact_error(self, ex):
            dialog = QtWidgets.QMessageBox()
            dialog.setWindowTitle("Error Adding Contact")
            dialog.setText(str(ex))
            dialog.exec()
            self.addContactButton.setDown(False)

        def no_contact_id_message(self):
            dialog = QMessageBox(self)
            dialog.setWindowTitle("No Contact ID")
            dialog.setText("Please add a contact ID")
            dialog.exec()
            self.addContactButton.setDown(False)

    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
