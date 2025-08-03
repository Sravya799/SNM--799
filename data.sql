-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: snmprjdb
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `filedata`
--

DROP TABLE IF EXISTS `filedata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `filedata` (
  `fid` int unsigned NOT NULL AUTO_INCREMENT,
  `file_name` varchar(20) NOT NULL,
  `file_data` longblob,
  `create_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `added_by` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fid`),
  KEY `added_by` (`added_by`),
  CONSTRAINT `filedata_ibfk_1` FOREIGN KEY (`added_by`) REFERENCES `users` (`useremail`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filedata`
--

LOCK TABLES `filedata` WRITE;
/*!40000 ALTER TABLE `filedata` DISABLE KEYS */;
INSERT INTO `filedata` VALUES (3,'addpet.html',_binary '<!DOCTYPE html>\r\n<html lang=\"en\">\r\n<head>\r\n    <meta charset=\"UTF-8\">\r\n    <title>Add New Pet</title>\r\n    <style>\r\n        body {\r\n            font-family: Arial, sans-serif;\r\n            background-color: black;\r\n            margin: 0;\r\n            padding: 0;\r\n        }\r\n        .container {\r\n            background-color:antiquewhite;\r\n            max-width: 500px;\r\n            margin: 50px auto;\r\n            padding: 30px;\r\n            border-radius: 10px;\r\n            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);\r\n        }\r\n        h1 {\r\n            text-align: center;\r\n            color: #333;\r\n            margin-bottom: 25px;\r\n        }\r\n        .form-group {\r\n            margin-bottom: 20px;\r\n        }\r\n        label {\r\n            display: block;\r\n            font-weight: bold;\r\n            margin-bottom: 8px;\r\n            color: #555;\r\n        }\r\n        input[type=\"text\"],\r\n        input[type=\"number\"] {\r\n            width: 100%;\r\n            padding: 10px;\r\n            border: 1px solid #ccc;\r\n            border-radius: 6px;\r\n            font-size: 16px;\r\n        }\r\n        .btn {\r\n            background-color: #4CAF50;\r\n            color: white;\r\n            padding: 12px 20px;\r\n            border: none;\r\n            border-radius: 6px;\r\n            cursor: pointer;\r\n            font-size: 16px;\r\n            width: 100%;\r\n        }\r\n        .btn:hover {\r\n            background-color: #45a049;\r\n        }\r\n        .link {\r\n            display: block;\r\n            text-align: center;\r\n            margin-top: 15px;\r\n            color: #007BFF;\r\n            text-decoration: none;\r\n        }\r\n        .link:hover {\r\n            text-decoration: underline;\r\n        }\r\n     \r\n    </style>\r\n</head>\r\n \r\n    <h2>Saved Pets</h2>\r\n    <ul>\r\n        {% for pet in pets %}\r\n        <li>{{ pet.name }} ({{ pet.species }}) - {{ pet.breed }} - Age: {{ pet.age }}</li>\r\n        {% endfor %}\r\n    </ul>\r\n    \r\n\r\n<body>\r\n     \r\n     \r\n    <div class=\"container\">\r\n        <h1>Add a New Pet</h1>\r\n        <form method=\"post\">\r\n            <div class=\"form-group\">\r\n                <label for=\"petName\">Pet Id:</label>\r\n                <input type=\"text\" id=\"pet_id\" name=\"id\" required>\r\n            </div>\r\n            <div class=\"form-group\">\r\n                <label for=\"species\">Species (e.g., Dog, Cat):</label>\r\n                <input type=\"text\" id=\"species\" name=\"species\" required>\r\n            </div>\r\n            <div class=\"form-group\">\r\n                <label for=\"breed\">Breed:</label>\r\n                <input type=\"text\" id=\"breed\" name=\"breed\">\r\n            </div>\r\n            <div class=\"form-group\">\r\n                <label for=\"age\">Age (Years):</label>\r\n                <input type=\"number\" id=\"age\" name=\"age\" min=\"0\">\r\n            </div>\r\n            <button type=\"submit\" class=\"btn\">Save Pet</button>\r\n\r\n            \r\n        </form>\r\n        <a href=\"{{ url_for(\'dashboard\') }}\" class=\"link\">Back to Dashboard</a>\r\n        <a href=\"{{ url_for(\'dashboard\') }}\" class=\"back_btn\">Back to Dashboard</a>\r\n        <a href=\"{{url_for(\'view_more\',pet_id=pet[\'id\'])}}\"></a>\r\n        <a href=\"{{ url_for(\'addpet\') }}\">Add Another Pet</a>\r\n    </div>\r\n   \r\n</body>\r\n</html>\r\n','2025-08-03 22:27:40','sravyasravs492@gmail.com'),(4,'app (1).py',_binary 'from flask import Flask,request,render_template,url_for,redirect,flash\r\napp=Flask(__name__)\r\nusers={}\r\npets={}\r\n@app.route(\'/\')\r\ndef home():\r\n    return render_template(\'welcome.html\')\r\n@app.route(\'/register\',methods=[\'GET\',\'POST\'])\r\ndef register():\r\n    if request.method==\'POST\':\r\n        print(request.form)\r\n        username=request.form[\'username\']\r\n        email=request.form[\'email\']\r\n        password=request.form[\'pwd\']    \r\n        number=request.form[\'phoneno\']    \r\n        if email not in users:\r\n            users[email]={\'username\':username,\'password\':password,\'number\':number}\r\n            print(users)\r\n            return redirect(url_for(\'login\'))\r\n        else:\r\n            return \'already existed\'\r\n\r\n    return render_template(\'register.html\')\r\n@app.route(\'/login\',methods=[\'GET\',\'POST\'])\r\ndef login():\r\n    if request.method==\'POST\':\r\n        uemail=request.form[\'uemail\']\r\n        password=request.form[\'password\']\r\n        if uemail in users:\r\n            if users[uemail][\'password\']==password:\r\n                current_user= uemail\r\n                return redirect(url_for(\'dashboard\',current_user=uemail))\r\n            else:\r\n                return \'password wrong\'\r\n        else:\r\n            return \'wrong email\'\r\n        \r\n    return render_template(\'login.html\')\r\n@app.route(\'/dashboard/<current_user>\')\r\ndef dashboard(current_user):\r\n    if not current_user:\r\n\r\n        return redirect(url_for(\"login\"))\r\n    user_pets = {pid: pdata for pid, pdata in pets.items() if pdata[\'owner\'] == current_user()}\r\n    return render_template(\'dashboard.html\', pets=user_pets,current_user=current_user)\r\n@app.route(\'/addpet\', methods=[\'GET\', \'POST\'])\r\ndef addpet():\r\n    if request.method == \'POST\':\r\n        pet_id=request.form[\'id\']\r\n        \r\n        species = request.form[\'species\']\r\n        breed = request.form[\'breed\']\r\n        age = request.form[\'age\']\r\n        \r\n\r\n        pets[pet_id] = {\r\n            \r\n            \'species\': species,\r\n            \'breed\': breed,\r\n            \'age\': age,\r\n            \'owner\': current_user()\r\n        }\r\n        print(pets)\r\n        \r\n        return redirect(url_for(\"dashboard\"))\r\n    return render_template(\'addpet.html\')\r\n\r\n@app.route(\'/viewpet\')\r\ndef viewpet():\r\n    if not current_user():\r\n        return redirect(url_for(\"login\"))\r\n    user_pets = {pid: pdata for pid, pdata in pets.items() if pdata[\'owner\'] == current_user()}\r\n    return render_template(\'viewpet.html\', pets=user_pets)\r\n\r\n@app.route(\'/delete/<current_user>\')\r\ndef delete(current_user):\r\n    return render_template(\'delete.html\')\r\n\r\n@app.route(\'/logout\')\r\ndef logout():\r\n   \r\n    flash(\'Logged out.\')\r\n    return redirect(url_for(\'login\'))\r\napp.run(debug=True,use_reloader=True)','2025-08-03 23:00:45','sravyasravs492@gmail.com'),(5,'register (2).html',_binary '<!DOCTYPE html>\r\n<html lang=\"en\">\r\n<head>\r\n    <meta charset=\"UTF-8\">\r\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\r\n    <title>PawPal Registration</title>\r\n    <style>\r\n        body {\r\n            margin: 0;\r\n            padding: 0;\r\n            background: url(\'/static/pet3.jpg\') no-repeat center center fixed;\r\n            background-size: cover;\r\n            font-family: Arial, sans-serif;\r\n            color: white;\r\n        }\r\n\r\n        .form-container {\r\n            background-color:darkgrey; /* translucent background */\r\n            padding: 30px;\r\n            border-radius: 10px;\r\n            width: 300px;\r\n            margin: 80px auto;\r\n            text-align: center;\r\n        }\r\n\r\n        input[type=\"text\"],\r\n        input[type=\"email\"],\r\n        input[type=\"number\"],\r\n        input[type=\"password\"] {\r\n            width: 100%;\r\n            padding: 10px;\r\n            margin: 10px 0;\r\n            border: none;\r\n            border-radius: 5px;\r\n        }\r\n\r\n        button {\r\n            width: 100px;\r\n            padding: 10px;\r\n            background-color: #6a1b9a;\r\n            color: white;\r\n            border: none;\r\n            border-radius: 5px;\r\n            margin-top: 15px;\r\n            cursor: pointer;\r\n        }\r\n\r\n        button:hover {\r\n            background-color: #8e24aa;\r\n        }\r\n\r\n        h1 {\r\n            margin-bottom: 20px;\r\n        }\r\n\r\n        marquee {\r\n            font-weight: bold;\r\n        }\r\n    </style>\r\n</head>\r\n<body>\r\n    <div class=\"form-container\">\r\n        <h1><marquee>Be a reason as pets forever home 🖤</marquee></h1>\r\n        <form method=\"post\">\r\n            <label>Enter Username:</label><br>\r\n            <input type=\"text\" name=\"username\" placeholder=\"ex.puji\"><br>\r\n\r\n            <label>Enter Email Id:</label><br>\r\n            <input type=\"email\" name=\"email\" placeholder=\"email\"><br>\r\n\r\n            <label>Enter Phone No:</label><br>\r\n            <input type=\"number\" name=\"phoneno\" placeholder=\"Ph.no\"><br>\r\n\r\n            <label>Enter Password:</label><br>\r\n            <input type=\"password\" name=\"pwd\" placeholder=\"password\"><br>\r\n\r\n            <a href=\"{{url_for(\'login\')}}\"><button>Submit</button></a>\r\n        </form>\r\n    </div>\r\n</body>\r\n</html>\r\n','2025-08-04 00:58:54','sravyasravs492@gmail.com');
/*!40000 ALTER TABLE `filedata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notes`
--

DROP TABLE IF EXISTS `notes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notes` (
  `nid` int unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `create_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `added_by` varchar(50) NOT NULL,
  PRIMARY KEY (`nid`),
  KEY `added_by` (`added_by`),
  CONSTRAINT `notes_ibfk_1` FOREIGN KEY (`added_by`) REFERENCES `users` (`useremail`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notes`
--

LOCK TABLES `notes` WRITE;
/*!40000 ALTER TABLE `notes` DISABLE KEYS */;
INSERT INTO `notes` VALUES (4,'python','Simple and Easy','2025-08-03 16:56:25','angirekulasravya4@gmail.com'),(5,'Mysql','tables ','2025-08-04 00:57:26','sravyasravs492@gmail.com');
/*!40000 ALTER TABLE `notes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `username` varchar(30) NOT NULL,
  `useremail` varchar(60) NOT NULL,
  `password` varchar(20) DEFAULT NULL,
  `gender` enum('female','male','other') DEFAULT NULL,
  PRIMARY KEY (`useremail`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('sravya','angirekulasravya4@gmail.com','1234','female'),('sravya','Sravyasravs492@gmail.com','1234','female');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-04  1:34:10
