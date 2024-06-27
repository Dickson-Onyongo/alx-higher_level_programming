-- script that creates the database hbtn_0d_2 and the user user_0d_2.
-- User_0d_2 should have only SELECT privilege in the database hbtn_0d_2
-- The user_0d_2 password should be set to user_0d_2_pwd
-- If the database hbtn_0d_2 already exists, your script should not fail
-- If the user user_0d_2 already exists, your script should not fail

CREATE IF NOT EXIST DATABASE hbtn_0d_2;
CREATE IF NOT EXIST USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT TO 'hbtn_0d_2'@'localhost' WITH GRANT OPTION;
