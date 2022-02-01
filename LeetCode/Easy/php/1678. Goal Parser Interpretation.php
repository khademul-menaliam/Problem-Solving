function interpret($command) {
       return str_replace(['()', '(al)'], ['o', 'al'], $command);
       

    }