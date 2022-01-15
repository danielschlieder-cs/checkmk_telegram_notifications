
INSTALL_PREFIX = $(OMD_ROOT)/local/share/check_mk/

install:
	echo "Installing into $(INSTALL_PREFIX)"
	install "notifications/telegram" "$(INSTALL_PREFIX)/notifications/"
	install "web/plugins/wato/telegram.py" "$(INSTALL_PREFIX)/web/plugins/wato/"
