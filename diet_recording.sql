-- Create the Users table
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    age INT,
    gender ENUM('Male', 'Female', 'Other'),
    height DECIMAL(5,2),
    weight DECIMAL(5,2),
    CHECK (age > 0 AND age < 120),
    CHECK (height > 0),
    CHECK (weight > 0)
);

-- Create the Foods table
CREATE TABLE IF NOT EXISTS Foods (
    food_id INT PRIMARY KEY AUTO_INCREMENT,
    food_name VARCHAR(100) NOT NULL,
    serving_size VARCHAR(50),
    calories DECIMAL(6,2),
    protein DECIMAL(6,2),
    carbohydrates DECIMAL(6,2),
    fat DECIMAL(6,2),
    fiber DECIMAL(6,2),
    sugar DECIMAL(6,2),
    sodium DECIMAL(6,2),
    cholesterol DECIMAL(6,2)
);

-- Create the Meals table
CREATE TABLE IF NOT EXISTS Meals (
    meal_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    meal_date DATE NOT NULL,
    meal_type ENUM('Breakfast', 'Lunch', 'Dinner', 'Snack') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Create the MealDetails table
CREATE TABLE IF NOT EXISTS MealDetails (
    meal_detail_id INT PRIMARY KEY AUTO_INCREMENT,
    meal_id INT NOT NULL,
    food_id INT NOT NULL,
    quantity DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (meal_id) REFERENCES Meals(meal_id),
    FOREIGN KEY (food_id) REFERENCES Foods(food_id)
);

-- Create the Goals table
CREATE TABLE IF NOT EXISTS Goals (
    goal_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    daily_calories DECIMAL(6,2),
    daily_protein DECIMAL(6,2),
    daily_carbohydrates DECIMAL(6,2),
    daily_fat DECIMAL(6,2),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

INSERT INTO Users (username, email, password, age, gender, height, weight)
VALUES 
('john_doe', 'john@example.com', 'encrypted_password', 30, 'Male', 175.5, 70.2),
('jane_smith', 'jane@example.com', 'encrypted_password', 28, 'Female', 165.0, 60.0),
('alex_yu', 'alex@example.com', 'encrypted_password',20,'Male', 175.0, 65.0);

INSERT INTO Foods (food_name, serving_size, calories, protein, carbohydrates, fat, fiber, sugar, sodium, cholesterol)
VALUES 
('Apple', '1 medium (182g)', 95, 0.5, 25, 0.3, 4.4, 19, 1.8, 0),
('French Fries', '1 medium (117g)', 365, 4.0, 63, 12.0, 6.0, 0.0, 2.0, 0),
('Chicken Breast', '100g', 165, 31, 0, 3.6, 0, 0, 74, 85),
('Brown Rice', '1 cup (195g)', 216, 5.0, 45, 1.8, 3.5, 1.0, 10, 0),
('Broccoli', '1 cup (91g)', 31, 2.5, 6, 0.3, 2.4, 1.5, 30, 0),
('Almonds', '1 oz (28g)', 164, 6.0, 6, 14.0, 3.5, 1.2, 0, 0);

-- Meals for john_doe on 2023-10-15
INSERT INTO Meals (user_id, meal_date, meal_type)
VALUES 
(1, '2023-10-15', 'Breakfast'),
(1, '2023-10-15', 'Lunch'),
(1, '2023-10-15', 'Dinner'),
(2, '2023-10-15', 'Breakfast'),
(3, '2023-10-15', 'Breakfast'),
(3, '2023-10-15', 'Lunch'),
(3, '2023-10-15', 'Snack');

-- MealDetails for Breakfast (meal_id = 1)
INSERT INTO MealDetails (meal_id, food_id, quantity)
VALUES 
(1, 1, 1.0),  -- 1 serving of Apple
(1, 5, 0.5);  -- 0.5 serving of Almonds

-- MealDetails for Lunch (meal_id = 2)
INSERT INTO MealDetails (meal_id, food_id, quantity)
VALUES 
(2, 2, 1.0),  -- 1 serving of Chicken Breast
(2, 3, 1.0);  -- 1 serving of Brown Rice

-- MealDetails for Dinner (meal_id = 3)
INSERT INTO MealDetails (meal_id, food_id, quantity)
VALUES 
(3, 2, 1.0),  -- 1 serving of Chicken Breast
(3, 4, 2.0);  -- 2 servings of Broccoli

-- MealDetails for Snack (meal_id = 4)
INSERT INTO MealDetails (meal_id, food_id, quantity)
VALUES 
(4, 6, 1.0);  -- 1 serving of Almonds

INSERT INTO Goals (user_id, daily_calories, daily_protein, daily_carbohydrates, daily_fat)
VALUES 
(1, 2000, 100, 250, 70);

CREATE VIEW DailySummary AS
SELECT 
    u.user_id,
    u.username,
    m.meal_date,
    SUM(f.calories * md.quantity) AS total_calories,
    SUM(f.protein * md.quantity) AS total_protein,
    SUM(f.carbohydrates * md.quantity) AS total_carbohydrates,
    SUM(f.fat * md.quantity) AS total_fat
FROM 
    Users u
    JOIN Meals m ON u.user_id = m.user_id
    JOIN MealDetails md ON m.meal_id = md.meal_id
    JOIN Foods f ON md.food_id = f.food_id
    -- link the tables together
GROUP BY 
    u.user_id, m.meal_date;

CREATE INDEX idx_users_user_id ON Users(user_id);
CREATE INDEX idx_users_username ON Users(username);
CREATE INDEX idx_meals_user_id ON Meals(user_id);
CREATE INDEX idx_meals_meal_date ON Meals(meal_date);
CREATE INDEX idx_mealdetails_meal_id ON MealDetails(meal_id);
CREATE INDEX idx_mealdetails_food_id ON MealDetails(food_id);
CREATE INDEX idx_foods_food_name ON Foods(food_name);

SELECT 
    u.username,
    m.meal_date,
    SUM(f.calories * md.quantity) AS total_calories,
    SUM(f.protein * md.quantity) AS total_protein,
    SUM(f.carbohydrates * md.quantity) AS total_carbohydrates,
    SUM(f.fat * md.quantity) AS total_fat
FROM 
    Users u
    JOIN Meals m ON u.user_id = m.user_id
    JOIN MealDetails md ON m.meal_id = md.meal_id
    JOIN Foods f ON md.food_id = f.food_id
WHERE 
    u.user_id = 1 AND m.meal_date = '2023-10-15'
GROUP BY 
    u.username, m.meal_date;

-- compare the user's daily goals with their actual intake
SELECT 
    g.daily_calories,
    di.total_calories,
    (di.total_calories - g.daily_calories) AS calorie_difference,
    g.daily_protein,
    di.total_protein,
    (di.total_protein - g.daily_protein) AS protein_difference,
    g.daily_carbohydrates,
    di.total_carbohydrates,
    (di.total_carbohydrates - g.daily_carbohydrates) AS carbohydrate_difference,
    g.daily_fat,
    di.total_fat,
    (di.total_fat - g.daily_fat) AS fat_difference
FROM 
    Goals g
    JOIN (
        SELECT 
            u.user_id,
            SUM(f.calories * md.quantity) AS total_calories,
            SUM(f.protein * md.quantity) AS total_protein,
            SUM(f.carbohydrates * md.quantity) AS total_carbohydrates,
            SUM(f.fat * md.quantity) AS total_fat
        FROM 
            Users u
            JOIN Meals m ON u.user_id = m.user_id
            JOIN MealDetails md ON m.meal_id = md.meal_id
            JOIN Foods f ON md.food_id = f.food_id
        WHERE 
            u.user_id = 1 AND m.meal_date = '2023-10-15'
        GROUP BY 
            u.user_id
    ) di ON g.user_id = di.user_id
WHERE 
    g.user_id = 1;

-- Retreive daily summary
SELECT * FROM DailySummary
WHERE user_id = 1 AND meal_date = '2023-10-15';
