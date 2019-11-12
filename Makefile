watch: clean
	# nohup bash -c 'cd backdrop-theme && grunt serve' &
	nohup bash -c 'cd src && make devserver' &
	sleep 5
	xdg-open http://localhost:8000/
	tail -f nohup.out

kill:
	nohup bash -c 'pgrep -f grunt | xargs kill -9' &
	nohup bash -c 'pgrep -f pelican | xargs kill -9' &

restart: kill watch

lint:
	find src/content -name '*.rst' | parallel rst-lint '{}'

clean:
	rm -rf output
	rm -f nohup.out
