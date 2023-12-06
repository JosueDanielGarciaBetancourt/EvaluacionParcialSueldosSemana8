CREATE DATABASE dbCalculoSueldo2
GO

USE dbCalculoSueldo2
GO

CREATE TABLE tblBonificacion(
    IDBonificacion VARCHAR(8) PRIMARY KEY,
    bonTipo VARCHAR(40),
    bonValor FLOAT NOT NULL
)

CREATE TABLE tblMes(
    IDMes VARCHAR(8) PRIMARY KEY,
    mesNombre VARCHAR(40) NOT NULL
)

CREATE TABLE Empleado(
    ID INT PRIMARY KEY,
    NombreCompleto VARCHAR(70),
    Sueldo DECIMAL(7, 2),
    Cargo VARCHAR(90)
)

CREATE TABLE tblBoletaPago(
    IDBoleta VARCHAR(8) PRIMARY KEY,
    bolSueldoNeto FLOAT,
    bolDescuentoTotal FLOAT,
    bolBonificacionTotal FLOAT,
    bolFechaEmision DATE,
    IDEmpleado INT NOT NULL,
    FOREIGN KEY (IDEmpleado) REFERENCES Empleado(ID)
)

CREATE TABLE tblDetalleBonificacion(
    IDBoleta VARCHAR(8) NOT NULL,
    IDBonificacion VARCHAR(8) NOT NULL,
    detbonMontoTotalBonificacion FLOAT,
    FOREIGN KEY (IDBonificacion) REFERENCES tblBonificacion(IDBonificacion),
    FOREIGN KEY (IDBoleta) REFERENCES tblBoletaPago(IDBoleta)
)

CREATE TABLE tblDetalleMensualTrabajador(
    IDEmpleado INT NOT NULL,
    IDMes VARCHAR(8) NOT NULL,
    detailAnio CHAR(8),
    detailHorasExtra INT,
    detailMinutosTardanzas INT,
    detailMinutosJustificados INT,
    detailDiasFalta INT,
    detailDiasJustificados INT,
    detailSueldoNeto FLOAT,
    FOREIGN KEY (IDEmpleado) REFERENCES Empleado(ID),
    FOREIGN KEY (IDMes) REFERENCES tblMes(IDMes)
)


-- Insertar registros en tblBonificacion
INSERT INTO tblBonificacion (IDBonificacion, bonTipo, bonValor) VALUES
('BON001', 'Bonificaci�n 1', 500.00),
('BON002', 'Bonificaci�n 2', 300.00),
('BON003', 'Bonificaci�n 3', 250.00),
('BON004', 'Bonificaci�n 4', 400.00),
('BON005', 'Bonificaci�n 5', 600.00);

-- Insertar registros en tblMes
INSERT INTO tblMes (IDMes, mesNombre) VALUES
('MES001', 'Enero'),
('MES002', 'Febrero'),
('MES003', 'Marzo'),
('MES004', 'Abril'),
('MES005', 'Mayo');

-- Insertar registros en Empleado
INSERT INTO Empleado (ID, NombreCompleto, Sueldo, Cargo) VALUES
(1, 'Juan P�rez', 3000.00, 'Gerente'),
(2, 'Mar�a L�pez', 2500.00, 'Asistente'),
(3, 'Carlos G�mez', 3500.00, 'Analista'),
(4, 'Ana Rodr�guez', 2800.00, 'Asistente'),
(5, 'Luis Mart�nez', 4000.00, 'Gerente');

-- Insertar registros en tblBoletaPago
INSERT INTO tblBoletaPago (IDBoleta, bolSueldoNeto, bolDescuentoTotal, bolBonificacionTotal, bolFechaEmision, IDEmpleado) VALUES
('BP001', 2700.00, 100.00, 200.00, '2023-11-01', 1),
('BP002', 2200.00, 90.00, 150.00, '2023-11-01', 2),
('BP003', 3200.00, 120.00, 250.00, '2023-11-01', 3),
('BP004', 2500.00, 100.00, 180.00, '2023-11-01', 4),
('BP005', 3700.00, 150.00, 300.00, '2023-11-01', 5);

-- Insertar registros en tblDetalleBonificacion
INSERT INTO tblDetalleBonificacion (IDBoleta, IDBonificacion, detbonMontoTotalBonificacion) VALUES
('BP001', 'BON001', 200.00),
('BP002', 'BON002', 150.00),
('BP003', 'BON003', 250.00),
('BP004', 'BON004', 180.00),
('BP005', 'BON005', 300.00);

-- Insertar registros en tblDetalleMensualTrabajador
INSERT INTO tblDetalleMensualTrabajador (IDEmpleado, IDMes, detailAnio, detailHorasExtra, detailMinutosTardanzas, detailMinutosJustificados, detailDiasFalta, detailDiasJustificados, detailSueldoNeto) VALUES
(1, 'MES001', '2023', 10, 30, 15, 2, 3, 2700.00),
(2, 'MES002', '2023', 5, 20, 10, 1, 2, 2200.00),
(3, 'MES003', '2023', 15, 40, 25, 3, 4, 3200.00),
(4, 'MES004', '2023', 7, 25, 12, 1, 1, 2500.00),
(5, 'MES005', '2023', 20, 50, 30, 4, 5, 3700.00);

Select * from Empleado;

select *
from Empleado

-- Crear el inicio de sesi�n
CREATE LOGIN Pier2 WITH PASSWORD = '123';

-- Crear el usuario asociado al inicio de sesi�n en la base de datos "Sueldos"

CREATE USER Pier2 FOR LOGIN Pier2;

-- Asignar el rol db_owner al usuario Pier en la base de datos "Sueldos"
EXEC sp_addrolemember 'db_owner', 'Pier2';