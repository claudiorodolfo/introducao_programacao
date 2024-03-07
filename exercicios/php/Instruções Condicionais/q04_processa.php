<?php
	$valor = $_POST['valor'];
	
	if (valor >= 1 && valor <= 10) {
		print 'Alimentação';
	}
	
	if (valor >= 11 && valor <= 20) {
		print 'Limpeza';
	}

	if (valor >= 21 && valor <= 30) {
		print 'Eletrônicos';
	}	
?>