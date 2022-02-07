from sys import maxsize


class Contact:
    def __init__(self, contact_id=None, firstname=None, middlename=None, lastname=None, nickname=None, title=None
                 , company=None, address=None, home_telephone=None, mobile_telephone=None, work_telephone=None,
                 fax_telephone=None, email=None, email_2=None,
                 email_3=None, home_page_url=None, birthday=None, birth_month=None, birth_year=None, address_2=None,
                 home_telephone_2=None, notes=None, group=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None, all_addresses_from_details_page=None):
        self.id = contact_id
        self.firstname = firstname
        self.middle_name = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_telephone = home_telephone
        self.mobile_telephone = mobile_telephone
        self.work_telephone = work_telephone
        self.fax_telephone = fax_telephone
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3
        self.home_page_url = home_page_url
        self.birthday = birthday
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.address_2 = address_2
        self.home_telephone_2 = home_telephone_2
        self.notes = notes
        self.group = group
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_addresses_from_details_page = all_addresses_from_details_page

    def __repr__(self):
        return "|   %s   |   %s   |   %s   |   %s   |   %s   |   %s   |   %s   |   %s   |" % (
            str(self.id), self.firstname, self.lastname, self.address,
            self.email, self.home_telephone, self.mobile_telephone, self.work_telephone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.lastname == other.lastname or self.lastname is None or
                other.lastname is None) and \
               (self.firstname == other.firstname or self.firstname is None or
                other.firstname is None)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
