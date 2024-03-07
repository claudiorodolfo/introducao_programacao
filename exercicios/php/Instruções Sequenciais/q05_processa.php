<?php
	$valor1 = $_POST['valor1'];
	$valor2 = $_POST['valor2'];
	
	print 'Antes da troca';
	print 'Valor1: ' . $valor1 . ', Valor2: ' . $valor2;
	
	$auxiliar = $valor1;
	$valor1 = $valor2;
	$valor2 = $auxiliar;
	
	print 'Depois da troca';
	print 'Valor1: ' . $valor1 . ', Valor2: ' . $valor2;
?>