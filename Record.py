import processing
def save_data(Rec):
    save_record_data = []
    for i in range(len(Rec)):
        save_record_data.append(Rec.pop("id", "secondname", "name", "lastname", "phone_number", "comment"))
    return save_record_data

