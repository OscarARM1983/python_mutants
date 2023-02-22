-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 22-02-2023 a las 17:23:28
-- Versión del servidor: 8.0.17
-- Versión de PHP: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dna_meli`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dna_verificados`
--

CREATE TABLE `dna_verificados` (
  `id` int(11) NOT NULL,
  `dna0` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `dna1` text COLLATE utf8_spanish_ci NOT NULL,
  `dna2` text COLLATE utf8_spanish_ci NOT NULL,
  `dna3` text COLLATE utf8_spanish_ci NOT NULL,
  `dna4` text COLLATE utf8_spanish_ci NOT NULL,
  `dna5` text COLLATE utf8_spanish_ci NOT NULL,
  `mutante` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `dna_verificados`
--

INSERT INTO `dna_verificados` (`id`, `dna0`, `dna1`, `dna2`, `dna3`, `dna4`, `dna5`, `mutante`) VALUES
(1, 'ATGCGA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG', 1),
(2, 'ATGCGA', 'CAGTGC', 'TTATTT', 'AGACGG', 'GCGTCA', 'TCACTG', 0),
(3, 'AAAAGA', 'CAGGGG', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG', 1),
(4, 'ATGCGA', 'CAGTGC', 'TTATGT', 'ATGCGA', 'CAGTGC', 'TCACTG', 0),
(5, 'ATGCGA', 'CAGTGC', 'TTAGGT', 'AGAAGG', 'CCCCTG', 'TCACTG', 1),
(6, 'ATGCGA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTA', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `dna_verificados`
--
ALTER TABLE `dna_verificados`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `dna_verificados`
--
ALTER TABLE `dna_verificados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
