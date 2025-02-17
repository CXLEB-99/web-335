// 1. Display all students
db.students.find().pretty()

// 2. Add a new student
db.students.insertOne({
  firstName: "New",
  lastName: "Student",
  studentId: "s1019",
  houseId: "h1007"
})

// Verify the student was added
db.students.find({ studentId: "s1019" }).pretty()

// 3. Update the last name of the student added in step 2
db.students.updateOne(
  { studentId: "s1019" },
  { $set: { lastName: "Updated" } }
)

// Verify the student’s last name was updated
db.students.find({ studentId: "s1019" }).pretty()

// 4. Delete the student added in step 2
db.students.deleteOne({ studentId: "s1019" })

// Verify the student was deleted
db.students.find({ studentId: "s1019" }).pretty()

// 5. Display all students by house (Sorted by houseId)
db.students.aggregate([
  { $lookup: {
      from: "houses",
      localField: "houseId",
      foreignField: "houseId",
      as: "houseDetails"
  }},
  { $sort: { houseId: 1 } }
])

// 6. Display all students in Gryffindor (houseId: h1007)
db.students.aggregate([
  { $match: { houseId: "h1007" } }
])

// 7. Display all students in the house with an Eagle mascot
db.students.aggregate([
  {
    $lookup: {
      from: "houses",
      localField: "houseId",
      foreignField: "houseId",
      as: "houseDetails"
    }
  },
  {
    $match: {
      "houseDetails.mascot": "Eagle"
    }
  }
])
