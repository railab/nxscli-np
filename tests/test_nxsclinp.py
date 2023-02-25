import nxscli_np
import nxscli_np.plugin


def test_nxsclinp():
    assert nxscli_np.__version__

    assert isinstance(nxscli_np.plugin.plugins_list, list)
    assert isinstance(nxscli_np.plugin.configs_list, list)
