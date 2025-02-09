// Caleb Goforth - Hands-On 5.1
// MongoDB Document Manipulation and Projections

// 1. Insert a new user
db.users.insertOne({
    firstName: "John",
    lastName: "Doe",
    email: "johndoe@example.com",
    age: 30
  });
  
  // 2. Update Mozart’s email address
  db.users.updateOne(
    { firstName: "Mozart" },
    { $set: { email: "mozart@me.com" } }
  );
  
  // 3. Show all users with only first name, last name, and email
  db.users.find({}, { firstName: 1, lastName: 1, email: 1, _id: 0 });
  