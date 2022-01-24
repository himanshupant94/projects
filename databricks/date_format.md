# Introduction

- UTC to PT Timezone conversion
- Difference between conversion of timezone using **extract** & **date_format** function

### SQL using extract function
```
select concat(extract(month from (from_utc_timestamp(current_timestamp ,'America/Los_Angeles'))) 
, '/',extract(day from (from_utc_timestamp(current_timestamp
,'America/Los_Angeles'))),'/',extract(year from (from_utc_timestamp(current_timestamp 
,'America/Los_Angeles'))),' ',extract(hour from (from_utc_timestamp(current_timestamp
,'America/Los_Angeles'))),':',extract(minutes from (from_utc_timestamp(current_timestamp 
,'America/Los_Angeles')))) InvoicedDate
```

**Screenshot**

![image](https://user-images.githubusercontent.com/10596429/150872049-d8accb48-19de-4e31-9174-f9a7bc555b73.png)



### SQL using date_format function
```
select date_format(from_utc_timestamp(current_timestamp,'America/Los_Angeles'), 'MM/dd/yy HH:mm') InvoicedDate
```

**Screenshot**


![image](https://user-images.githubusercontent.com/10596429/150873508-4a3d4470-abdf-4d91-a689-6332e9473e2e.png)


