CREATE TABLE files (
    id INT AUTO_INCREMENT PRIMARY KEY,
    smiles VARCHAR(255),
    concentration FLOAT
);

INSERT INTO files (smiles, concentration) VALUES
('C(C(=O)O)N', 0.1),
('CCO', 0.2),
('CCCC', 0.3);