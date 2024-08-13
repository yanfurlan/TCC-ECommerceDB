
# ECommerceDB

Este projeto cria um banco de dados para um sistema de e-commerce usando SQLite e Python. Ele inclui a criação de tabelas, inserção de dados e consultas ao banco de dados.

## Arquivos

### 1. `create_tables.py`

Este arquivo cria as tabelas necessárias no banco de dados SQLite. As tabelas incluem `Categories`, `Suppliers`, `Products`, `Customers`, `Orders`, e `OrderItems`.

#### Como usar:
Execute o seguinte comando no terminal:

```bash
python create_tables.py
```

### 2. `insert_data.py`

Este arquivo insere dados nas tabelas do banco de dados SQLite. As inserções incluem categorias, fornecedores, produtos e clientes.

#### Como usar:
Execute o seguinte comando no terminal:

```bash
python insert_data.py
```

### 3. `query_data.py`

Este arquivo realiza consultas no banco de dados SQLite e exibe os resultados. As consultas incluem a listagem de todos os produtos e clientes.

#### Como usar:
Execute o seguinte comando no terminal:

```bash
python query_data.py
```

### 4. `visualize_data.py`

Esse arquivo retorna com o graficos sobre os produtos. 

#### Como usar:
Execute o seguinte comando no terminal:

```bash
python visualize_data.py
```

## SQL para Bancos de Dados Tradicionais

Se você estiver usando um serviço de banco de dados SQL tradicional (como MySQL, PostgreSQL, etc.), você pode usar os comandos SQL fornecidos no arquivo `database_creation.sql` para criar e inserir dados no banco de dados.

### 1. `database_creation.sql`

Este arquivo contém todos os comandos SQL necessários para criar o banco de dados e tabelas, além de inserir dados. Você pode executar este script em qualquer serviço de banco de dados SQL instalado.

#### Como usar:

1. Abra seu cliente de banco de dados SQL.
2. Crie um novo banco de dados chamado `ECommerceDB`.
3. Execute o script `database_creation.sql`.

```sql
-- Criação do banco de dados
CREATE DATABASE ECommerceDB;

-- Seleciona o banco de dados
USE ECommerceDB;

-- Criação da tabela de categorias
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL
);

-- Criação da tabela de fornecedores
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT,
    SupplierName VARCHAR(255) NOT NULL,
    ContactName VARCHAR(255),
    ContactEmail VARCHAR(255)
);

-- Criação da tabela de produtos
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    SupplierID INT,
    CategoryID INT,
    UnitPrice DECIMAL(10, 2),
    Stock INT,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

-- Criação da tabela de clientes
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20)
);

-- Criação da tabela de pedidos
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT,
    OrderDate DATE NOT NULL,
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Criação da tabela de itens do pedido
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT,
    ProductID INT,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Inserção de dados na tabela de categorias
INSERT INTO Categories (CategoryName)
VALUES ('Electronics'), ('Books'), ('Clothing'), ('Home & Kitchen');

-- Inserção de dados na tabela de fornecedores
INSERT INTO Suppliers (SupplierName, ContactName, ContactEmail)
VALUES ('Supplier One', 'John Doe', 'john@example.com'),
       ('Supplier Two', 'Jane Smith', 'jane@example.com');

-- Inserção de dados na tabela de produtos
INSERT INTO Products (ProductName, SupplierID, CategoryID, UnitPrice, Stock)
VALUES ('Laptop', 1, 1, 1000.00, 50),
       ('Smartphone', 1, 1, 500.00, 100),
       ('Novel', 2, 2, 20.00, 200),
       ('T-shirt', 2, 3, 15.00, 150);

-- Inserção de dados na tabela de clientes
INSERT INTO Customers (CustomerName, Email, Phone)
VALUES ('Alice Johnson', 'alice@example.com', '555-1234'),
       ('Bob Smith', 'bob@example.com', '555-5678');
```

## Requisitos

- Python 3.x
- SQLite3

## Como Executar

1. Clone este repositório.
2. Execute `create_tables.py` para criar as tabelas.
3. Execute `insert_data.py` para inserir os dados.
4. Execute `query_data.py` para consultar os dados.
5. Execute `visualize_data.py` para consultar os dados.
## Autor

Este projeto foi criado como um exemplo de uso de SQLite com Python para a criação e manipulação de um banco de dados de e-commerce.