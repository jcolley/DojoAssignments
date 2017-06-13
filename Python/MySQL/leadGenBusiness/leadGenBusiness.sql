#SELECT MONTHNAME(billing.charged_datetime) AS month, SUM(billing.amount) AS total_revenue FROM billing WHERE MONTHNAME(billing.charged_datetime) = 'MARCH';

#SELECT billing.client_id, SUM(billing.amount) AS total_revenue FROM billing WHERE billing.client_id = 2;

#SELECT sites.client_id, sites.domain_name FROM sites WHERE sites.client_id = 2;

#SELECT sites.domain_name, COUNT(sites.site_id) AS total, MONTHNAME(sites.created_datetime) AS month, YEAR(sites.created_datetime) AS year FROM sites WHERE sites.client_id = 1 GROUP BY MONTHNAME(sites.created_datetime) ORDER BY YEAR(sites.created_datetime);

#SELECT sites.domain_name AS website, COUNT(leads.leads_id) AS number_of_leads, DATE(leads.registered_datetime) AS date_generated FROM leads LEFT JOIN sites ON leads.site_id = sites.site_id WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-02-15' GROUP BY sites.site_id;

#SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS name, COUNT(leads.leads_id) as number_of_leads FROM clients LEFT JOIN sites ON clients.client_id = sites.client_id LEFT JOIN leads ON sites.site_id = leads.site_id WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31' GROUP BY sites.site_id;

#SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS name, COUNT(leads.leads_id) as number_of_leads, MONTHNAME(leads.registered_datetime) AS month_generated FROM clients LEFT JOIN sites ON clients.client_id = sites.client_id LEFT JOIN leads ON sites.site_id = leads.site_id WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-06-30' GROUP BY sites.site_id;

#