import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env { VIRT_DB: D1Database; AI: any; }
const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// NOIZYLAB OS - VIRTUALIZATION WORKER
const VIRTUALIZATION = {
    history: {
        ibm_cp40: { name: 'IBM CP-40', year: 1967, significance: 'First VM system' },
        ibm_vm370: { name: 'IBM VM/370', year: 1972, significance: 'Commercial virtualization' },
        vmware_workstation: { name: 'VMware Workstation', year: 1999, significance: 'x86 virtualization' }
    },
    hypervisors: {
        type1: {
            name: 'Type 1 (Bare Metal)',
            examples: {
                vmware_esxi: { name: 'VMware ESXi', year: 2001, significance: 'Enterprise standard' },
                hyper_v: { name: 'Microsoft Hyper-V', year: 2008 },
                xen: { name: 'Xen', year: 2003, significance: 'Open source, AWS foundation' },
                kvm: { name: 'KVM', year: 2007, significance: 'Linux kernel virtualization' },
                proxmox: { name: 'Proxmox VE', year: 2008, significance: 'Open-source virtualization platform' }
            }
        },
        type2: {
            name: 'Type 2 (Hosted)',
            examples: {
                vmware_workstation: { name: 'VMware Workstation/Fusion' },
                virtualbox: { name: 'VirtualBox', developer: 'Oracle', significance: 'Free, cross-platform' },
                parallels: { name: 'Parallels Desktop', significance: 'Mac virtualization leader' },
                qemu: { name: 'QEMU', significance: 'Emulation + virtualization' }
            }
        }
    },
    containers: {
        docker: { name: 'Docker', year: 2013, significance: 'Containerization revolution' },
        kubernetes: { name: 'Kubernetes', year: 2014, developer: 'Google', significance: 'Container orchestration standard' },
        containerd: { name: 'containerd', significance: 'Container runtime' },
        podman: { name: 'Podman', developer: 'Red Hat', significance: 'Daemonless containers' },
        lxc: { name: 'LXC', year: 2008, significance: 'Linux containers' },
        cri_o: { name: 'CRI-O', significance: 'Kubernetes container runtime' }
    },
    cloud: {
        aws_ec2: { name: 'AWS EC2', year: 2006, significance: 'First major cloud compute' },
        azure_vms: { name: 'Azure Virtual Machines' },
        gcp_compute: { name: 'Google Compute Engine' },
        openstack: { name: 'OpenStack', year: 2010, significance: 'Open-source cloud platform' }
    },
    microVMs: {
        firecracker: { name: 'Firecracker', year: 2018, developer: 'AWS', significance: 'Lambda/Fargate backend' },
        kata_containers: { name: 'Kata Containers', significance: 'Secure container runtime' },
        gvisor: { name: 'gVisor', developer: 'Google', significance: 'User-space kernel sandbox' }
    },
    technologies: {
        intel_vtx: { name: 'Intel VT-x', year: 2005, significance: 'Hardware virtualization' },
        amd_v: { name: 'AMD-V', year: 2006, significance: 'AMD hardware virtualization' },
        arm_virt: { name: 'ARM Virtualization Extensions', significance: 'ARM hardware virtualization' },
        iommu: { name: 'IOMMU (VT-d/AMD-Vi)', significance: 'Device passthrough' },
        sr_iov: { name: 'SR-IOV', significance: 'Hardware network virtualization' }
    }
};

app.get('/api/virtualization/categories', (c) => c.json({ success: true, categories: Object.keys(VIRTUALIZATION) }));
app.get('/api/virtualization/:cat', (c) => {
    const cat = c.req.param('cat') as keyof typeof VIRTUALIZATION;
    return VIRTUALIZATION[cat] ? c.json({ success: true, data: VIRTUALIZATION[cat] }) : c.json({ error: 'Not found' }, 404);
});
app.get('/health', (c) => c.json({ status: 'healthy', worker: 'virtualization-worker' }));

export default app;
