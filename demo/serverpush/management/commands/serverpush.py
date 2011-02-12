from django.core.management.base import BaseCommand, CommandError

from demo.serverpush.management.server import HookboxServer

class Command(BaseCommand):
	def handle(self, *args, **options):
		server = HookboxServer()
		try:
			server.run().wait()
		except KeyboardInterrupt:
			print "Ctr+C pressed; Exiting."
