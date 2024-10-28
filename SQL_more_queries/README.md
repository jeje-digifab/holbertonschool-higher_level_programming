# MySQL Queries and User Management Tasks
## Tasks Summary

#### 0. My privileges!
- **Description**: Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in localhost).
- **File**: `0-privileges.sql`
- **Repo**: `holbertonschool-higher_level_programming/SQL_more_queries`

#### 1. Root user
- **Description**: Write a script that creates the MySQL server user `user_0d_1` with all privileges. The user's password should be set to `user_0d_1_pwd`. If the user already exists, the script should not fail.
- **File**: `1-create_user.sql`
- **Repo**: `holbertonschool-higher_level_programming/SQL_more_queries`

#### 2. Read user
- **Description**: Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`. The user should have only SELECT privilege in the database `hbtn_0d_2`. The user's password should be set to `user_0d_2_pwd`. If the database or user already exists, the script should not fail.
- **File**: `2-create_read_user.sql`
- **Repo**: `holbertonschool-higher_level_programming/SQL_more_queries`

#### 3. Always a name
- **Description**: Write a script that creates the table `force_name` on your MySQL server. The table should have columns `id` (INT) and `name` (VARCHAR(256) can’t be null). If the table already exists, the script should not fail.
- **File**: `3-force_name.sql`
- **Repo**: `holbertonschool-higher_level_programming/SQL_more_queries`

#### 4. ID can't be null
- **Description**: Write a script that creates the table `id_not_null` on your MySQL server. The table should have columns `id` (INT with default value 1) and `name` (VARCHAR(256)). If the table already exists, the script should not fail.
- **File**: `4-never_empty.sql`
- **Repo**: `holbertonschool-higher_level_programming/SQL_more_queries`

#### 5. Unique ID
- **Description**: Write a script that creates the table `unique_id` on your MySQL server. The table should have columns `id` (INT with default value 1 and must be unique) and `name` (VARCHAR(256)). If the table already exists, the script should not fail.
- **File**: `5-unique_id.sql`
- **Repo**: `holbertonschool-higher_level_programming/SQL_more_queries`

#### 6. States table
- **Description**: Write a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server. The table should have columns `id` (INT unique, auto generated, can’t be null and is a primary key) and `name` (VARCHAR(256) can’t be null). If the database or table already exists, the script should not fail.
- **File**: `6-states.sql`
- **Repo**: `holbertonschool-higher_level_programming/SQL_more_queries`

#### 7. Cities table
- **Description**: Write a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server. The table should have columns `id` (INT unique, auto generated, can’t be null and is a primary key), `state_id` (INT, can’t be null and must be a FOREIGN KEY that references to `id` of the `states` table), and `name` (VARCHAR(256) can’t be null). If the database or table already exists, the script should not fail.
- **File**: `7-cities.sql`
- **Repo**: `holbertonschool-higher_level_programming/SQL_more_queries`

#### 8. Cities of California
- **Description**: Write a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`. Results must be sorted in ascending order by `cities.id`. The database name will be passed as an argument of the mysql command.
- **File**: `8-cities_of_california_subquery.sql`
- **Repo**: `holbertonschool-higher_level_programming/SQL_more_queries`

#### 9. Cities by States
- **Description**: Write a script that lists all cities contained in the database `hbtn_0d_usa`. Each record should display: `cities.id - cities.name - states.name`. Results must be sorted in ascending order by `cities.id`. The database name will be passed as an argument of the mysql command.
- **File**: `9-cities_by_state_join.sql`
- **Repo**: `holbertonschool-higher_level_programming/SQL_more_queries`

#### 10. Genre ID by show
- **Description**: Import the database dump from `hbtn_0d_tvshows` to your MySQL server. Write a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked. Each record should display: `tv_shows.title - tv_show_genres.genre_id`. Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`. The database name will be passed as an argument of the mysql command.
- **File**: `10-genre_id_by_show.sql`
- **Repo**: `holbertonschool-higher_level_programming/SQL_more_queries`

#### 11. Genre ID for all shows
- **Description**: Import the database dump of `hbtn_0d_tvshows` to your MySQL server. Write a script that lists all shows contained in the database `hbtn_0d_tvshows`. Each record should display: `tv_shows.title - tv_show_genres.genre_id`. Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`. If a show doesn’t have a genre, display `NULL`. The database name will be passed as an argument of the mysql command.
- **File**: `11-genre_id_all_shows.sql`
- **Repo**: `holbertonschool-higher_level_programming/SQL_more_queries`

#### 12. No genre
- **Description**: Import the database dump from `hbtn_0d_tvshows` to your MySQL server. Write a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked. Each record should display: `tv_shows.title - tv_show_genres.genre_id`. Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`. The database name will be passed as an argument of the mysql command.
- **File**: `12-no_genre.sql`
- **Repo**: `holbertonschool-higher_level_programming/SQL_more_queries`

#### 13. Number of shows by genre
- **Description**: Import the database dump from `hbtn_0d_tvshows` to your MySQL server. Write a script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each. Each record should display: `<TV Show genre> - <Number of shows linked to this genre>`. Results must be sorted in descending order by the number of shows linked. The database name will be passed as an argument of the mysql command.
- **File**: `13-count_shows_by_genre.sql`
- **Repo**: `holbertonschool-higher_level_programming/SQL_more_queries`

#### 14. My genres
- **Description**: Import the database dump from `hbtn_0d_tvshows` to your MySQL server. Write a script that uses the `hbtn_0d_tvshows` database to list all genres of the show Dexter. Each record should display: `tv_genres.name`. Results must be sorted in ascending order by the genre name. The database name will be passed as an argument of the mysql command.
- **File**: `14-my_genres.sql`
- **Repo**: `holbertonschool-higher_level_programming/SQL_more_queries`

#### 15. Only Comedy
- **Description**: Import the database dump from `hbtn_0d_tvshows` to your MySQL server. Write a script that lists all Comedy shows in the database `hbtn_0d_tvshows`. Each record should display: `tv_shows.title`. Results must be sorted in ascending order by the show title. The database name will be passed as an argument of the mysql command.
- **File**: `15-comedy_only.sql`
- **Repo**: `holbertonschool-higher_level_programming/SQL_more_queries`

#### 16. List shows and genres
- **Description**: Import the database dump from `hbtn_0d_tvshows` to your MySQL server. Write a script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`. If a show doesn’t have a genre, display `NULL` in the genre column. Each record should display: `tv_shows.title - tv_genres.name`. Results must be sorted in ascending order by the show title and genre name. The database name will be passed as an argument of the mysql command.
- **File**: `16-shows_by_genre.sql`
- **Repo**: `holbertonschool-higher_level_programming/SQL_more_queries`

