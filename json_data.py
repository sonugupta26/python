
# profile = {
#     "name": "Ram",
#     "gender":"male",
#     "education":[
#         {"collage": "abc collage", "level": "+2"},
#         {"collage": "xyz collage", "level": "bachlor"},
#     ],
#     "addresh":[
#         {
#             "temporary":{
#                 "ward": 1,
#                 "city": "ktm",
#             },
#             "permanent":{
#                 "ward": 2,
#                 "city": "birgunj",
#             }
#         }
#     ]

# }
# print(f"name-{profile.get('name')}")
# print(f"gender:{profile.get('gender')}")
# educations =profile.get("education")
# # print(educations)
# for education in educations:
#     # print(education)
#     # print(education.get("collage"), education.get("level;"))
#       print(f"collage:{education.get('collage')} and level:{education.get('level')}")

# addreshes = profile.get("addresh")
# for addresh in addreshes:
#         abc = addresh.get("temporary")
#         for i in abc.items():
#             print(i)


        # for v,k in val.items():
        #      print(v,k)







students = {
    "count": 2,
    "data": [
        {
            "name": "Ram",
            "address": "Tinknune",
            "course": "Python Django",
            "attendance": [
                {
                    "month": "January",
                    "total_working_days": 25,
                    "present": 24,
                    "absent": 1,
                    "leave": 0,
                },
                {
                    "month": "February",
                    "total_working_days": 28,
                    "present": 20,
                    "absent": 2,
                    "leave": 6,
                }
            ]
        },
        {
            "name": "Hari",
            "address": "Tinknune",
            "course": "Python Django",
            "attendance": [
                {
                    "month": "January",
                    "total_working_days": 25,
                    "present": 23,
                    "absent": 1,
                    "leave": 1,
                },
                {
                    "month": "February",
                    "total_working_days": 28,
                    "present": 27,
                    "absent": 0,
                    "leave": 1,
                }
            ]
        }
    ]
}


print(f"count-{students.get('count')}")
alldata = students.get("data")
# print(alldata)
for data in alldata:
    print(data['name'],data['address'])
# #     for key,val in data.items():
# #         print(key,val)
       
# students = students.get("data")
# # print(students)
# for student in students:
#     stu = student.get("attendance")
#     for attendence in stu:
#         print(attendence.get("month"), attendence.get("total_working_days"), attendence.get("present"), attendence.get("absent"), attendence.get("leave"))
