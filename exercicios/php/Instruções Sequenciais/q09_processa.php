<?php
	$valor1 = $_POST['valor1'];
	$valor2 = $_POST['valor2'];
	$resultado = round($valor1/$valor2);
	print 'Resultado: ' . $resultado;
?>