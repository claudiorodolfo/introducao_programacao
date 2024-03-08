<?php
	$item = $_POST['item'];
	$sorteio = rand(0,2);
	//0-Pedra, 1-Papel, 2-Tesoura
	switch($sorteio) {
		case 0:
			$itemComputador = 'Pedra';
			break;
		case 1:
			$itemComputador = 'Papel';
			break;
		case 2:
			$itemComputador = 'Tesoura';
	}

	print 'Escolhi:' . $item . '<br>';
	print 'Comput.:' . $itemComputador . '<br>';

	if ($item == $itemComputador) {
		print 'Empate!';
	} else if ($item == 'Pedra' && $itemComputador == 'Papel' ||
			$item == 'Papel' && $itemComputador == 'Tesoura' ||
			$item == 'Tesoura' && $itemComputador == 'Pedra') {
		print 'Computador Ganhou!';
	} else {
		print 'Você Ganhou!';
	}
?>