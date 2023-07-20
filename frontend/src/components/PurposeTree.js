import React, {useContext, useEffect, useState} from "react";
import {TreeContext} from "../TreeContext";
import {
    Chip,
    Dialog,
    DialogActions,
    DialogContent,
    DialogTitle,
    FormControlLabel,
    IconButton,
    Typography
} from "@mui/material";
import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";
import ArrowRightIcon from "@mui/icons-material/ArrowRight";
import TreeView from "@mui/lab/TreeView";
import TreeItem from "@mui/lab/TreeItem";
import Checkbox from "@mui/material/Checkbox";
import AddCircleOutlineIcon from "@mui/icons-material/AddCircleOutline";
import RemoveCircleOutlineIcon from "@mui/icons-material/RemoveCircleOutline";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";

const PurposeTree = ({settingsView = false}) => {
    const {treeData, handleCheckboxChange, handleAddNodeContext, handleDeleteNodeContext} = useContext(TreeContext);
    const [expanded, setExpanded] = useState([]);
    const [dialogOpen, setDialogOpen] = useState(false);
    const [newNodeParentId, setNewNodeParentId] = useState(null);
    const [purposeName, setPurposeName] = useState('');
    const [description, setDescription] = useState('');
    const [transformations, setTransformations] = useState({
        REMOVEBG: false,
        BLACKWHITE: true,
        BLUR: true,
        REDACT_EMAIL: true
    });

    const handleAddNode = (nodeId) => {
        setNewNodeParentId(nodeId);
        setDialogOpen(true);
    };

    const handleDialogClose = () => {
        setPurposeName('');
        setDescription('');
        setTransformations({
            REMOVEBG: false,
            BLACKWHITE: false,
            BLUR: false,
            REDACT_EMAIL: false
        });
        setDialogOpen(false);
    };


    const handleDialogConfirm = () => {
        // The selected transformations are those with a true value
        const selectedTransformations = Object.keys(transformations).filter(key => transformations[key]);

        handleAddNodeContext(newNodeParentId, purposeName, description, selectedTransformations);
        handleDialogClose();
    };


    useEffect(() => {
        const getAllNodeIds = (nodes) => {
            return nodes.reduce((acc, node) => {
                return [...acc, node.purpose_id.toString(), ...getAllNodeIds(node.children || [])];
            }, []);
        };
        setExpanded(getAllNodeIds(treeData));
    }, [treeData]);

    const renderLabel = (node) => {
        const disabled = !node.parentSelected;
        return (
            <div style={{display: "flex", flexDirection: "column"}}>
                <div style={{display: "flex", alignItems: "center", justifyContent: "space-between"}}>
                    <div style={{display: "flex", alignItems: "center"}}>
                        <Checkbox
                            checked={node.selected}
                            onChange={() => handleCheckboxChange(node.purpose_id)}
                            color="primary"
                            disabled={disabled}
                        />
                        <div style={{color: disabled ? "grey" : "inherit"}}>{node.name}</div>
                    </div>
                    {settingsView && (
                        <div>
                            <IconButton color="primary" onClick={() => handleAddNode(node.purpose_id)}>
                                <AddCircleOutlineIcon/>
                            </IconButton>
                            <IconButton color="secondary" onClick={() => handleDeleteNodeContext(node.purpose_id)}>
                                <RemoveCircleOutlineIcon/>
                            </IconButton>
                        </div>
                    )}
                </div>
                <Typography variant="body2" color="textSecondary">{node.description}</Typography>
                <div style={{marginTop: "8px"}}>
                    Transformations:
                    {node.transformations.map((transformation) => (
                        <Chip key={transformation} label={transformation} color={"primary"}/>
                    ))}
                </div>
            </div>
        );
    };

    const renderTree = (nodes, parentSelected = true) =>
        nodes.map((node) => (
            <TreeItem
                key={node.purpose_id}
                nodeId={node.purpose_id.toString()}
                label={renderLabel({...node, parentSelected: node.selected && parentSelected})}
            >
                {Array.isArray(node.children) ? renderTree(node.children, node.selected && parentSelected) : null}
            </TreeItem>
        ));

    return (
        <div>
            <TreeView
                defaultCollapseIcon={<ArrowDropDownIcon/>}
                defaultExpandIcon={<ArrowRightIcon/>}
                expanded={expanded}
                multiSelect
            >
                {renderTree(treeData)}
            </TreeView>
            <Dialog open={dialogOpen} onClose={handleDialogClose}>
                <DialogTitle>Add new node</DialogTitle>
                <DialogContent>
                    <TextField
                        value={purposeName}
                        onChange={(event) => setPurposeName(event.target.value)}
                        label="Purpose name"
                        fullWidth
                    />
                    <TextField
                        value={description}
                        onChange={(event) => setDescription(event.target.value)}
                        label="Description"
                        fullWidth
                    />
                    {/* Here you should add a checkbox for each possible transformation. */}
                    {Object.keys(transformations).map((key) => (
                        <FormControlLabel
                            control={
                                <Checkbox
                                    checked={transformations[key]}
                                    onChange={(event) => setTransformations({
                                        ...transformations,
                                        [key]: event.target.checked
                                    })}
                                    color="primary"
                                />
                            }
                            label={key}
                        />
                    ))}
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleDialogClose} color="primary">
                        Cancel
                    </Button>
                    <Button onClick={handleDialogConfirm} color="primary">
                        Add
                    </Button>
                </DialogActions>
            </Dialog>
        </div>
    );
};

export default PurposeTree;
