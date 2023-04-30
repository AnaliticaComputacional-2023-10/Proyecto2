
CREATE TABLE personas (
    age INT,
    sex INT,
    cp INT,
    trestbps INT,
    chol INT,
    fbs INT,
    restecg INT,
    thalach INT,
    exang INT,
    oldpeak INT,
    slope INT,
    ca INT,
    thal INT,
    heartdis INT
);
INSERT INTO personas (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, heartdis) VALUES
(4, 1, 1, 2, 1, 1, 2, 1, 0, 5, 3, 0, 6, 0),
(4, 1, 4, 2, 2, 0, 2, 1, 1, 4, 2, 3, 3, 1),
(4, 1, 4, 1, 1, 0, 2, 1, 1, 5, 2, 2, 7, 1),
(1, 1, 3, 1, 2, 0, 0, 2, 0, 5, 3, 0, 3, 0),
(1, 0, 2, 1, 1, 0, 2, 2, 0, 3, 1, 0, 3, 0),
(3, 1, 2, 1, 1, 0, 0, 2, 0, 2, 1, 0, 3, 0),
(4, 0, 4, 2, 2, 0, 2, 2, 0, 5, 3, 2, 3, 1),
(3, 0, 4, 1, 2, 0, 0, 2, 1, 2, 1, 0, 3, 0),
(4, 1, 4, 1, 2, 0, 2, 1, 0, 3, 2, 1, 7, 1),
(2, 1, 4, 2, 1, 1, 2, 2, 1, 5, 3, 0, 7, 1),
(3, 1, 4, 2, 1, 0, 0, 1, 0, 1, 2, 0, 6, 0),
(3, 0, 2, 2, 2, 0, 2, 2, 0, 3, 2, 0, 3, 0),
(3, 1, 3, 1, 2, 1, 2, 1, 1, 2, 2, 1, 6, 1),
(1, 1, 2, 1, 2, 0, 0, 2, 0, 1, 1, 0, 7, 0),
(2, 1, 3, 2, 1, 1, 0, 2, 0, 2, 1, 0, 7, 0),
(3, 1, 3, 2, 1, 0, 0, 2, 0, 4, 1, 0, 3, 0),
(2, 1, 2, 1, 1, 0, 0, 2, 0, 3, 3, 0, 7, 1),
(2, 1, 4, 2, 1, 0, 0, 2, 0, 3, 1, 0, 3, 0),
(2, 0, 3, 1, 2, 0, 0, 1, 0, 1, 1, 0, 3, 0),
(2, 1, 2, 1, 2, 0, 0, 2, 0, 2, 1, 0, 3, 0),
(4, 1, 1, 1, 1, 0, 2, 1, 1, 4, 2, 0, 3, 0),
(3, 0, 1, 2, 2, 1, 2, 2, 0, 3, 1, 0, 3, 0),
(3, 1, 2, 1, 2, 0, 2, 2, 0, 4, 2, 0, 3, 1),
(3, 1, 3, 2, 1, 0, 2, 2, 0, 5, 1, 2, 7, 1),
(3, 1, 4, 1, 1, 0, 2, 1, 1, 5, 2, 2, 7, 1),
(2, 0, 3, 1, 1, 0, 0, 2, 0, 4, 2, 0, 3, 0),
(3, 0, 3, 1, 2, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(4, 0, 1, 2, 1, 0, 0, 1, 0, 5, 3, 0, 3, 0),
(1, 1, 4, 2, 2, 0, 0, 2, 0, 4, 1, 0, 3, 0),
(1, 1, 4, 1, 1, 0, 2, 1, 1, 5, 2, 0, 7, 1),
(4, 0, 1, 2, 1, 0, 0, 1, 0, 4, 1, 2, 3, 0),
(3, 1, 4, 1, 1, 1, 0, 2, 1, 3, 1, 2, 7, 1),
(4, 1, 3, 2, 2, 0, 0, 2, 0, 1, 1, 0, 3, 1),
(3, 1, 4, 2, 1, 0, 0, 2, 0, 2, 2, 0, 7, 0),
(1, 1, 3, 1, 1, 0, 0, 2, 1, 1, 1, 0, 3, 0),
(1, 1, 4, 2, 1, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(1, 1, 4, 1, 1, 0, 2, 1, 1, 5, 2, 0, 7, 1),
(3, 1, 4, 2, 2, 0, 2, 1, 1, 2, 2, 1, 6, 1),
(2, 1, 4, 2, 2, 0, 0, 1, 1, 3, 2, 1, 7, 1),
(4, 1, 3, 2, 1, 1, 0, 1, 1, 3, 2, 0, 3, 0),
(4, 0, 4, 2, 1, 0, 2, 1, 0, 3, 2, 3, 7, 1),
(1, 1, 1, 2, 1, 0, 0, 2, 1, 3, 1, 0, 7, 0),
(4, 0, 2, 2, 2, 0, 0, 2, 0, 1, 1, 2, 3, 0),
(3, 1, 3, 2, 1, 1, 0, 2, 0, 4, 1, 0, 3, 0),
(4, 0, 4, 1, 2, 0, 2, 2, 0, 1, 1, 0, 3, 1),
(3, 1, 3, 1, 1, 0, 2, 2, 0, 5, 2, 1, 7, 1),
(2, 1, 3, 1, 1, 0, 0, 1, 0, 2, 1, 0, 3, 0),
(2, 1, 4, 2, 1, 0, 2, 1, 0, 5, 2, 0, 7, 1),
(4, 0, 3, 2, 2, 1, 2, 2, 0, 2, 1, 1, 3, 0),
(2, 1, 3, 1, 1, 1, 2, 1, 0, 3, 3, 0, 3, 0),
(1, 0, 2, 1, 1, 0, 0, 2, 0, 1, 1, 1, 3, 0),
(4, 1, 4, 1, 1, 0, 0, 1, 0, 1, 1, 0, 7, 0),
(1, 1, 4, 1, 2, 0, 2, 2, 0, 1, 1, 1, 3, 1),
(1, 1, 2, 1, 1, 0, 2, 2, 0, 1, 1, 0, 3, 0),
(3, 1, 4, 1, 2, 0, 0, 1, 1, 3, 1, 1, 7, 1),
(2, 1, 4, 1, 2, 0, 2, 1, 1, 5, 2, 1, 7, 1),
(2, 1, 3, 2, 1, 0, 0, 2, 0, 2, 2, 1, 7, 1),
(1, 1, 4, 1, 1, 0, 2, 2, 0, 1, 1, 0, 7, 1),
(2, 1, 3, 1, 2, 0, 2, 1, 0, 2, 3, 1, 3, 0),
(2, 1, 1, 1, 1, 0, 2, 1, 1, 3, 1, 1, 3, 0),
(2, 0, 4, 1, 2, 0, 0, 1, 1, 3, 2, 0, 7, 1),
(1, 0, 3, 2, 1, 0, 2, 2, 1, 3, 3, 0, 3, 0),
(3, 1, 4, 1, 1, 0, 2, 1, 1, 5, 2, 3, 7, 1),
(2, 0, 3, 2, 2, 1, 0, 2, 0, 1, 1, 0, 3, 0),
(2, 1, 4, 1, 1, 0, 0, 1, 0, 3, 2, 1, 7, 1),
(3, 1, 4, 2, 2, 0, 2, 1, 1, 5, 2, 2, 7, 1),
(3, 1, 3, 2, 1, 0, 2, 2, 0, 5, 2, 0, 3, 1),
(2, 1, 3, 2, 1, 0, 2, 2, 0, 4, 1, 0, 7, 0),
(3, 1, 4, 2, 2, 0, 2, 1, 1, 5, 3, 0, 7, 1),
(1, 1, 3, 2, 1, 0, 0, 1, 0, 5, 2, 0, 3, 1),
(4, 0, 3, 2, 2, 0, 0, 1, 0, 2, 1, 0, 3, 0),
(4, 1, 4, 1, 2, 1, 0, 2, 0, 1, 2, 2, 7, 1),
(4, 1, 4, 1, 2, 0, 0, 1, 1, 4, 2, 2, 7, 1),
(4, 1, 4, 1, 2, 0, 2, 2, 0, 2, 1, 2, 6, 1),
(1, 1, 4, 1, 1, 0, 2, 2, 0, 1, 1, 1, 3, 1),
(4, 0, 3, 2, 2, 0, 2, 1, 0, 2, 1, 0, 3, 0),
(3, 1, 4, 1, 2, 0, 2, 1, 1, 5, 2, 1, 7, 1),
(2, 0, 3, 2, 2, 0, 2, 1, 0, 4, 1, 1, 3, 0),
(2, 1, 2, 1, 1, 0, 2, 2, 0, 1, 2, 0, 3, 0),
(3, 1, 4, 2, 2, 0, 2, 1, 1, 2, 1, 0, 7, 1),
(1, 1, 4, 1, 1, 0, 2, 1, 1, 5, 2, 0, 3, 0),
(2, 0, 4, 1, 2, 0, 2, 1, 0, 1, 2, 0, 3, 0),
(1, 1, 3, 2, 2, 0, 2, 2, 0, 1, 1, 0, 3, 0),
(4, 1, 3, 2, 2, 1, 2, 1, 1, 4, 2, 0, 7, 1),
(2, 1, 2, 1, 2, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(1, 1, 3, 2, 1, 0, 2, 2, 0, 1, 1, 0, 3, 0),
(1, 1, 3, 2, 2, 0, 2, 2, 0, 1, 1, 0, 3, 0),
(2, 0, 3, 1, 1, 0, 2, 1, 0, 1, 1, 0, 3, 0),
(2, 0, 4, 2, 1, 0, 2, 2, 0, 1, 1, 0, 3, 0),
(2, 0, 3, 1, 2, 0, 2, 1, 0, 2, 1, 0, 3, 0),
(4, 1, 4, 1, 2, 0, 2, 1, 0, 1, 2, 0, 3, 0),
(4, 0, 4, 2, 1, 0, 2, 1, 0, 5, 3, 3, 7, 1),
(4, 1, 3, 1, 1, 0, 0, 1, 0, 4, 2, 3, 7, 0),
(1, 0, 3, 1, 1, 0, 0, 2, 0, 2, 2, 0, 3, 0),
(4, 0, 3, 2, 2, 0, 2, 2, 0, 1, 1, 0, 3, 0),
(2, 1, 4, 1, 2, 0, 0, 2, 1, 1, 1, 1, 7, 1),
(3, 1, 4, 1, 1, 0, 2, 1, 1, 3, 2, 1, 7, 1),
(3, 0, 4, 2, 2, 0, 2, 2, 0, 5, 2, 2, 7, 1),
(2, 1, 2, 2, 1, 0, 0, 2, 0, 2, 1, 1, 3, 0),
(2, 1, 4, 1, 1, 0, 2, 2, 0, 1, 1, 0, 3, 0),
(1, 1, 4, 1, 2, 0, 2, 2, 0, 1, 1, 0, 3, 0),
(1, 1, 1, 1, 1, 0, 2, 2, 0, 1, 1, 0, 3, 0),
(3, 0, 4, 1, 2, 0, 2, 2, 0, 1, 1, 1, 3, 0),
(4, 0, 3, 1, 2, 1, 2, 1, 0, 1, 1, 1, 3, 0),
(2, 1, 3, 1, 1, 0, 0, 1, 0, 5, 2, 3, 7, 1),
(2, 1, 2, 1, 2, 0, 0, 2, 0, 1, 1, 0, 7, 0),
(3, 1, 4, 2, 1, 0, 0, 2, 1, 1, 1, 1, 7, 1),
(3, 1, 3, 1, 1, 0, 2, 1, 0, 1, 2, 1, 7, 1),
(4, 1, 4, 1, 2, 0, 0, 1, 1, 5, 2, 1, 7, 1),
(1, 1, 4, 1, 1, 0, 0, 1, 0, 3, 2, 0, 7, 1),
(4, 0, 4, 2, 2, 0, 2, 1, 1, 3, 2, 0, 7, 1),
(3, 1, 4, 1, 2, 1, 2, 1, 1, 3, 2, 1, 3, 1),
(2, 1, 1, 1, 1, 0, 2, 2, 0, 1, 2, 0, 6, 0),
(1, 0, 4, 2, 2, 1, 2, 1, 1, 5, 2, 0, 7, 1),
(4, 0, 3, 1, 2, 0, 0, 1, 0, 3, 2, 1, 7, 1),
(1, 1, 2, 2, 1, 0, 0, 1, 0, 1, 2, 0, 6, 0),
(3, 1, 3, 2, 1, 1, 2, 2, 0, 1, 1, 0, 3, 0),
(1, 0, 4, 2, 1, 0, 0, 2, 0, 3, 1, 0, 3, 0),
(4, 1, 4, 1, 2, 1, 2, 1, 1, 4, 1, 3, 7, 1),
(4, 1, 4, 2, 2, 0, 2, 1, 0, 5, 2, 1, 7, 1),
(2, 1, 4, 1, 2, 1, 2, 1, 1, 1, 1, 2, 7, 1),
(4, 0, 4, 2, 2, 0, 2, 2, 0, 5, 2, 3, 7, 1),
(2, 1, 3, 1, 1, 0, 0, 1, 1, 3, 2, 0, 3, 0),
(2, 1, 4, 2, 1, 0, 0, 1, 1, 5, 3, 0, 7, 1),
(4, 1, 1, 2, 2, 1, 2, 2, 0, 3, 2, 1, 3, 1),
(1, 0, 2, 1, 1, 0, 2, 2, 0, 2, 2, 0, 3, 0),
(3, 0, 4, 2, 2, 1, 2, 1, 1, 5, 3, 2, 7, 1),
(2, 1, 4, 1, 1, 0, 0, 1, 1, 5, 2, 1, 7, 1),
(1, 1, 2, 1, 1, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(4, 0, 4, 1, 1, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(2, 1, 3, 1, 2, 0, 2, 1, 0, 1, 2, 0, 7, 0),
(2, 1, 3, 1, 1, 0, 0, 2, 1, 1, 1, 1, 7, 0),
(1, 1, 2, 1, 1, 0, 2, 2, 0, 1, 1, 0, 3, 0),
(2, 1, 4, 2, 2, 0, 2, 2, 1, 1, 1, 0, 3, 0),
(1, 0, 3, 1, 1, 0, 0, 2, 0, 1, 2, 0, 3, 0),
(2, 0, 2, 2, 2, 0, 2, 2, 0, 3, 2, 0, 3, 0),
(4, 1, 4, 2, 1, 0, 0, 1, 1, 5, 3, 0, 7, 1),
(4, 1, 2, 1, 2, 0, 2, 1, 0, 3, 2, 1, 7, 1),
(1, 1, 4, 1, 1, 0, 0, 1, 1, 4, 2, 0, 7, 1),
(2, 1, 3, 1, 1, 1, 2, 2, 0, 5, 2, 0, 3, 0),
(3, 1, 2, 2, 1, 0, 0, 2, 1, 1, 1, 0, 3, 0),
(3, 1, 1, 2, 2, 0, 2, 2, 0, 1, 2, 0, 7, 1),
(2, 1, 2, 1, 1, 1, 0, 2, 0, 1, 1, 0, 3, 0),
(4, 1, 3, 1, 2, 0, 0, 1, 1, 4, 2, 0, 7, 1),
(3, 1, 3, 1, 1, 0, 2, 2, 1, 2, 2, 0, 7, 0),
(1, 1, 3, 1, 1, 0, 0, 1, 0, 1, 1, 0, 3, 1),
(3, 1, 4, 2, 2, 1, 2, 1, 0, 3, 2, 3, 7, 1),
(1, 1, 3, 1, 2, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(1, 1, 2, 1, 2, 0, 2, 2, 0, 1, 1, 0, 3, 0),
(3, 0, 3, 1, 2, 0, 0, 2, 0, 1, 1, 1, 3, 0),
(2, 1, 1, 2, 2, 1, 0, 2, 0, 3, 2, 0, 7, 0),
(1, 0, 4, 1, 2, 0, 2, 1, 0, 2, 2, 0, 3, 0),
(4, 0, 3, 1, 2, 0, 2, 2, 0, 4, 2, 0, 7, 0),
(2, 1, 4, 2, 2, 0, 2, 1, 1, 2, 2, 1, 7, 1),
(4, 1, 4, 1, 1, 0, 2, 1, 1, 5, 3, 1, 3, 1),
(4, 1, 4, 1, 2, 0, 2, 1, 0, 5, 2, 3, 3, 1),
(2, 1, 4, 2, 2, 0, 0, 2, 1, 4, 1, 0, 7, 1),
(3, 1, 4, 1, 2, 0, 2, 2, 0, 1, 1, 2, 7, 1),
(3, 1, 4, 2, 2, 0, 2, 2, 0, 3, 2, 2, 7, 1),
(4, 1, 3, 1, 2, 0, 0, 1, 0, 3, 1, 1, 7, 0),
(1, 1, 2, 1, 1, 1, 0, 2, 0, 1, 1, 0, 7, 0),
(4, 1, 4, 1, 2, 0, 2, 2, 1, 1, 1, 3, 3, 1),
(2, 0, 3, 1, 1, 0, 0, 2, 0, 4, 2, 0, 3, 0),
(3, 0, 4, 1, 2, 0, 2, 1, 0, 3, 2, 0, 3, 0),
(2, 1, 3, 1, 2, 1, 0, 2, 0, 1, 1, 2, 3, 0),
(3, 1, 4, 2, 1, 0, 0, 2, 1, 1, 1, 0, 7, 0),
(2, 1, 3, 2, 1, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(2, 0, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 3, 0),
(1, 1, 4, 1, 2, 0, 2, 2, 1, 1, 1, 0, 7, 1),
(1, 0, 2, 1, 1, 0, 0, 1, 0, 1, 2, 0, 3, 0),
(4, 1, 3, 2, 2, 0, 0, 1, 1, 5, 2, 1, 7, 1),
(2, 1, 4, 2, 1, 0, 2, 1, 1, 1, 1, 0, 7, 0),
(3, 0, 4, 2, 2, 0, 0, 1, 1, 1, 2, 0, 3, 1),
(4, 0, 4, 2, 2, 0, 2, 2, 0, 3, 2, 0, 3, 0),
(4, 1, 4, 2, 1, 0, 2, 1, 0, 5, 2, 2, 6, 1),
(3, 1, 4, 2, 2, 0, 0, 1, 1, 3, 2, 1, 7, 1),
(2, 1, 4, 1, 1, 1, 0, 1, 0, 1, 1, 3, 7, 0),
(3, 1, 4, 2, 1, 0, 2, 1, 1, 5, 2, 1, 6, 1),
(1, 1, 3, 1, 2, 0, 0, 2, 0, 4, 1, 1, 3, 0),
(2, 1, 3, 1, 1, 1, 2, 2, 0, 1, 1, 3, 3, 0),
(2, 1, 4, 1, 2, 0, 2, 2, 0, 2, 2, 0, 7, 1),
(3, 0, 4, 2, 2, 0, 2, 1, 1, 4, 2, 2, 7, 1),
(1, 1, 1, 2, 1, 0, 2, 2, 0, 2, 1, 2, 3, 0),
(3, 1, 1, 2, 2, 0, 2, 1, 0, 5, 3, 0, 7, 0),
(3, 0, 4, 2, 2, 0, 2, 2, 0, 1, 1, 0, 3, 1),
(4, 0, 2, 2, 1, 0, 0, 2, 0, 1, 1, 2, 3, 0),
(1, 1, 3, 1, 1, 1, 0, 2, 0, 2, 3, 0, 7, 0),
(4, 1, 2, 2, 1, 0, 0, 1, 1, 1, 2, 3, 6, 1),
(2, 1, 2, 2, 2, 0, 2, 2, 0, 1, 1, 1, 7, 1),
(4, 1, 3, 2, 2, 0, 2, 1, 0, 5, 2, 3, 7, 1),
(2, 1, 3, 1, 1, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(2, 1, 4, 2, 2, 0, 0, 1, 1, 5, 2, 3, 7, 1),
(1, 1, 4, 2, 2, 1, 2, 1, 1, 1, 2, 0, 7, 1),
(4, 0, 4, 2, 2, 1, 0, 1, 0, 4, 2, 3, 3, 1),
(4, 0, 3, 1, 1, 0, 2, 1, 0, 4, 2, 0, 3, 0),
(4, 1, 4, 1, 2, 0, 2, 1, 1, 2, 2, 2, 3, 1),
(4, 1, 1, 2, 1, 1, 2, 1, 0, 1, 2, 1, 3, 0),
(1, 0, 4, 2, 1, 0, 2, 1, 1, 1, 2, 0, 3, 0),
(2, 0, 2, 1, 1, 0, 0, 2, 0, 3, 1, 0, 3, 0),
(3, 1, 1, 2, 2, 0, 2, 1, 0, 1, 1, 0, 3, 1),
(2, 0, 4, 1, 2, 0, 2, 2, 0, 1, 1, 0, 3, 0),
(4, 0, 4, 2, 2, 0, 0, 2, 1, 1, 1, 0, 3, 0),
(3, 1, 3, 2, 1, 1, 0, 2, 0, 1, 1, 1, 7, 0),
(4, 0, 3, 2, 2, 0, 0, 1, 0, 1, 1, 0, 7, 0),
(1, 1, 4, 1, 1, 0, 0, 2, 0, 1, 1, 0, 7, 0),
(1, 1, 4, 2, 2, 0, 2, 1, 1, 1, 2, 3, 7, 1),
(3, 1, 4, 1, 2, 0, 2, 1, 1, 5, 2, 2, 7, 1),
(2, 1, 4, 2, 1, 0, 2, 1, 1, 2, 2, 0, 7, 1),
(2, 1, 2, 1, 2, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(4, 0, 4, 2, 1, 0, 0, 2, 1, 3, 2, 0, 3, 1),
(1, 0, 3, 1, 1, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(1, 1, 1, 1, 1, 0, 0, 2, 1, 5, 2, 0, 7, 1),
(1, 1, 3, 1, 1, 0, 2, 2, 0, 5, 2, 0, 3, 0),
(4, 0, 4, 2, 1, 1, 0, 2, 1, 3, 2, 2, 7, 1),
(2, 1, 4, 1, 1, 0, 0, 2, 0, 1, 1, 1, 3, 1),
(3, 1, 1, 1, 1, 0, 2, 2, 0, 4, 2, 0, 7, 0),
(1, 0, 2, 1, 1, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(1, 0, 4, 2, 1, 0, 2, 1, 1, 1, 2, 0, 3, 0),
(4, 0, 4, 1, 2, 0, 0, 1, 0, 5, 2, 2, 3, 0),
(3, 1, 4, 2, 2, 0, 2, 2, 0, 1, 1, 0, 3, 0),
(1, 0, 3, 1, 2, 0, 2, 2, 1, 1, 1, 0, 3, 0),
(2, 0, 3, 1, 2, 0, 2, 2, 0, 1, 1, 0, 3, 0),
(1, 0, 3, 1, 1, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(2, 1, 4, 1, 2, 0, 0, 1, 1, 5, 2, 2, 7, 1),
(4, 0, 4, 1, 2, 0, 0, 2, 1, 4, 2, 2, 3, 1),
(1, 0, 2, 1, 1, 0, 0, 2, 0, 2, 1, 0, 3, 0),
(1, 1, 4, 1, 1, 0, 0, 1, 0, 1, 1, 0, 3, 0),
(4, 0, 3, 2, 2, 0, 0, 2, 0, 1, 1, 1, 3, 0),
(2, 1, 4, 1, 1, 0, 2, 1, 1, 1, 2, 1, 3, 1),
(4, 1, 4, 1, 1, 0, 2, 1, 1, 1, 1, 1, 3, 1),
(2, 0, 3, 2, 1, 0, 2, 2, 0, 1, 2, 0, 3, 0),
(2, 0, 4, 2, 2, 0, 1, 1, 1, 5, 2, 0, 3, 1),
(2, 1, 3, 1, 1, 0, 2, 1, 0, 2, 1, 3, 3, 1),
(4, 0, 2, 1, 2, 0, 2, 1, 1, 1, 1, 1, 3, 0),
(2, 0, 3, 2, 1, 0, 0, 2, 0, 1, 1, 1, 3, 0),
(2, 1, 4, 1, 2, 0, 2, 1, 1, 5, 2, 2, 3, 1),
(3, 1, 4, 1, 2, 1, 2, 1, 1, 4, 3, 0, 7, 1),
(1, 1, 4, 1, 2, 0, 2, 1, 0, 2, 1, 0, 7, 1),
(2, 0, 2, 2, 2, 0, 0, 2, 0, 1, 2, 0, 3, 0),
(1, 1, 2, 1, 2, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(1, 1, 2, 1, 1, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(1, 0, 2, 1, 2, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(2, 0, 4, 1, 2, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(4, 1, 1, 2, 1, 0, 0, 1, 0, 5, 2, 2, 3, 1),
(3, 0, 3, 1, 1, 1, 0, 1, 0, 1, 1, 0, 3, 0),
(4, 1, 4, 1, 1, 0, 0, 1, 0, 3, 2, 0, 3, 1),
(3, 1, 4, 1, 1, 0, 0, 2, 0, 1, 1, 1, 7, 1),
(1, 1, 4, 1, 2, 0, 2, 1, 1, 3, 2, 1, 3, 1),
(2, 1, 4, 1, 1, 0, 0, 2, 0, 3, 1, 2, 7, 1),
(4, 1, 2, 1, 1, 1, 2, 1, 0, 1, 1, 0, 3, 0),
(3, 1, 4, 1, 1, 0, 0, 1, 1, 4, 2, 0, 6, 0),
(3, 1, 4, 2, 1, 0, 0, 1, 0, 5, 2, 1, 7, 1),
(4, 1, 4, 1, 2, 0, 0, 1, 1, 1, 2, 1, 7, 0),
(2, 0, 3, 1, 2, 0, 2, 2, 0, 2, 1, 0, 3, 0),
(1, 1, 4, 1, 2, 0, 0, 2, 0, 3, 2, 0, 3, 0),
(1, 0, 3, 1, 1, 0, 0, 2, 0, 1, 2, 0, 3, 0),
(4, 0, 4, 1, 1, 0, 0, 1, 0, 1, 1, 2, 3, 0),
(4, 0, 3, 2, 1, 0, 1, 1, 0, 3, 2, 0, 3, 0),
(4, 1, 2, 2, 1, 0, 2, 1, 0, 1, 1, 0, 3, 0),
(3, 1, 2, 1, 2, 0, 0, 1, 0, 1, 1, 0, 7, 1),
(1, 0, 3, 1, 1, 0, 0, 1, 0, 1, 2, 1, 3, 0),
(3, 0, 2, 2, 2, 1, 2, 1, 0, 1, 1, 2, 3, 1),
(3, 0, 1, 2, 1, 0, 0, 2, 0, 2, 1, 0, 3, 0),
(1, 1, 3, 1, 1, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(4, 1, 4, 2, 1, 0, 2, 1, 1, 5, 2, 1, 3, 1),
(1, 1, 4, 2, 2, 0, 0, 1, 1, 4, 2, 0, 6, 1),
(2, 1, 4, 1, 1, 1, 0, 2, 1, 3, 2, 0, 3, 1),
(3, 1, 3, 1, 1, 1, 0, 1, 0, 5, 2, 1, 6, 1),
(1, 1, 4, 2, 1, 0, 0, 2, 0, 1, 1, 0, 7, 1),
(1, 1, 3, 1, 1, 0, 0, 1, 0, 1, 1, 0, 3, 0),
(4, 1, 4, 2, 1, 0, 2, 1, 1, 4, 1, 1, 7, 1),
(4, 1, 4, 2, 1, 0, 2, 1, 0, 5, 1, 0, 6, 0),
(1, 1, 4, 2, 2, 0, 0, 1, 1, 4, 2, 2, 7, 1),
(4, 0, 4, 1, 1, 0, 0, 1, 0, 4, 2, 0, 3, 0),
(3, 1, 1, 2, 1, 0, 0, 2, 0, 2, 1, 2, 3, 1),
(4, 1, 1, 2, 1, 0, 2, 2, 0, 2, 2, 0, 7, 0),
(4, 0, 3, 2, 2, 0, 2, 1, 0, 1, 2, 1, 3, 0),
(1, 0, 3, 2, 1, 0, 0, 1, 0, 1, 2, 0, 3, 0),
(3, 1, 2, 2, 1, 0, 2, 2, 0, 1, 1, 1, 3, 1),
(3, 0, 4, 1, 1, 0, 0, 1, 0, 2, 2, 0, 3, 0),
(3, 1, 4, 1, 2, 0, 0, 1, 1, 5, 2, 1, 7, 1),
(1, 1, 3, 1, 2, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(2, 0, 4, 1, 1, 0, 1, 1, 1, 5, 2, 1, 7, 1),
(1, 1, 2, 1, 1, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(4, 1, 4, 2, 1, 0, 0, 2, 0, 1, 1, 1, 7, 1),
(3, 1, 4, 1, 2, 0, 1, 1, 0, 5, 3, 3, 6, 1),
(3, 0, 4, 2, 1, 1, 2, 1, 1, 5, 2, 2, 6, 1),
(3, 1, 2, 1, 1, 0, 0, 1, 0, 1, 2, 0, 7, 0),
(3, 1, 2, 1, 1, 0, 2, 2, 0, 1, 1, 0, 7, 0),
(3, 1, 2, 1, 1, 0, 0, 2, 0, 1, 3, 0, 3, 0),
(4, 1, 3, 2, 1, 0, 2, 1, 0, 2, 2, 0, 7, 1),
(2, 0, 2, 2, 2, 0, 0, 2, 0, 3, 1, 0, 3, 0),
(1, 1, 4, 1, 1, 0, 0, 1, 1, 5, 3, 0, 6, 1),
(4, 1, 4, 2, 1, 0, 2, 1, 1, 5, 1, 2, 7, 1),
(4, 0, 4, 1, 1, 0, 0, 1, 1, 1, 2, 0, 3, 1),
(1, 1, 2, 1, 1, 0, 0, 2, 0, 1, 1, 0, 3, 0),
(3, 1, 4, 2, 1, 1, 2, 1, 0, 3, 2, 2, 6, 1),
(3, 0, 4, 2, 1, 0, 0, 1, 1, 1, 2, 0, 7, 1),
(1, 1, 1, 1, 2, 0, 0, 1, 0, 3, 2, 0, 7, 1),
(4, 1, 4, 2, 1, 1, 0, 1, 0, 5, 2, 2, 7, 1),
(3, 1, 4, 1, 1, 0, 0, 1, 1, 3, 2, 1, 7, 1),
(3, 0, 2, 1, 1, 0, 2, 2, 0, 1, 2, 1, 3, 1),
(1, 1, 3, 2, 1, 0, 0, 2, 0, 1, 1, 0, 3, 0);