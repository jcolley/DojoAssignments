#SELECT countries.name, languages.language, languages.percentage FROM languages LEFT JOIN countries ON countries.id = country_id WHERE language = 'Slovene';

#SELECT countries.name as name, COUNT(cities.id) as count FROM cities LEFT JOIN countries ON countries.id = country_id GROUP BY name ORDER BY count DESC;

#SELECT cities.name, cities.population FROM cities LEFT JOIN countries ON countries.id = country_id WHERE cities.population > 500000 AND country_id = 136 ORDER BY  cities.population DESC;

#SELECT language, percentage FROM languages WHERE percentage > 89 ORDER BY percentage DESC;

#SELECT name, surface_area, population FROM countries WHERE surface_area < 501 AND population > 100000;

#SELECT name FROM countries WHERE government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75;

#SELECT countries.name, cities.name, cities.district, cities.population FROM cities LEFT JOIN countries ON countries.id = 9 WHERE district = 'Buenos Aires' AND cities.population > 500000;

#SELECT region, COUNT(*) as count FROM countries GROUP BY region ORDER BY count DESC;