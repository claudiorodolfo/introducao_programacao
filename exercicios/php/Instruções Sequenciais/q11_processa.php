<?php
	$valor1 = $_POST['valor1'];
	$valor2 = $_POST['valor2'];
	$valor3 = $_POST['valor3'];
	
	if ($valor1 <= $valor2 && $valor2 <= $valor3) {
		print 'Ordem Crescente';
	} else if ($valor1 >= $valor2 && $valor2 >= $valor3) {
		print 'Ordem Decrescente';
	} else {
		print 'Fora de Ordem';	
	}
?>