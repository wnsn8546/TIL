# 사전 설정

## 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

## Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

## table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
id PRIMARY KEY,        
sido INTEGER NOT NULL, 
gender INTEGER NOT NULL,
age INTEGER NOT NULL,  
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,   
va_left REAL NOT NULL, 
va_right REAL NOT NULL,

blood_pressure INTEGER 
NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);
```

# 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE age < 10;
```

```
COUNT(*)
--------
156277
```

### 3. 성별이 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE gender = 1;
```

```
COUNT(*)
--------
510689
```

### 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE smoking = 3 AND is_drinking = 1;
```

```
COUNT(*)
--------
150361
```

### 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE va_left >= 2.0 and va_right >= 2.0;
```

```
COUNT(*)
--------
2614
```

### 6. 시도(sido)를 모두 중복 없이 출력하시오.

```sql
SELECT DISTINCT sido FROM healthcare ORDER BY sido;
```

```
sido
----
11
26
27
28
29
30
31
36
41
42
43
44
45
46
47
48
49
```

### 자유롭게 조합해서 원하는 데이터를 출력해보세요.

> 예) 허리 둘레가 x이상이면서 몸무게가 y이하인 사람

1) 허리 둘레가 25이상이면서 몸무게가 80이하인 사람.

```sql
SELECT COUNT(*) FROM healthcare WHERE waist >= 25 and weight <= 80;
```

```
COUNT(*)
--------
935162
```

2) 키가 190이상이면서 몸무게가 100이상인 사람.

```sql
SELECT COUNT(*) FROM healthcare WHERE height >= 190 and weight >= 100;
```

```
COUNT(*)
--------
129
```

3) 허리둘레가 35이상이면서 혈압이 140이상인 사람.

```sql
SELECT COUNT(*) FROM healthcare WHERE waist >= 35 and blood_pressure >= 140;
```

```
COUNT(*)
--------
145819
```
4) 허리둘레가 28이하이면서 혈압이 140이상인 사람.

```sql
SELECT COUNT(*) FROM healthcare WHERE waist <= 28 and blood_pressure >= 140;
```

```
COUNT(*)
--------
0
```