<?php
	$valor = $_POST['valor'];
	
	if ($valor > 10000) {
		print 'Investimento Alto';
	else
		print 'Investimento Baixo';
	}
?>