import msgpack


class Frame:
    """
    A single CAN frame.
    """

    def __init__(self, id=0, data=None, extended=False,
                 transmission_request=False,
                 data_length=0):

        if data is None:
            data = bytes()

        if len(data) > 8:
            raise ValueError

        self.id = id

        self.data = data
        self.data_length = data_length

        if len(self.data) > 0:
            self.data_length = len(self.data)

        self.transmission_request = transmission_request
        self.extended = extended


def encode(frame):
    """
    Encodes the given frame to raw messagepack bytes.
    """
    packer = msgpack.Packer(use_bin_type=True)
    data = packer.pack(frame.extended)
    data = data + packer.pack(frame.transmission_request)
    data = data + packer.pack(frame.id)
    data += packer.pack(frame.data)

    return data


def decode(data):
    """
    Decodes the given messagepack bytes to a Frame object.
    """
    unpacker = msgpack.Unpacker()
    result = Frame()

    unpacker.feed(data)

    result.extended = unpacker.unpack()
    result.transmission_request = unpacker.unpack()
    result.id = unpacker.unpack()
    result.data = unpacker.unpack()

    return result
