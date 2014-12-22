from erlport.erlang import set_encoder, set_decoder

from lsci import decoders, encoders, logger, obj


def setup():
    logger.info("Setting up lsci Python ...")
    obj.init()
    setup_encoders()
    setup_decoders()


def setup_encoders():
    set_encoder(encoders.all)


def setup_decoders():
    set_decoder(decoders.all)
