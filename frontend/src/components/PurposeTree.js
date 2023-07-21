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
        BLACKWHITE: false,
        EROSION: false,
        BLUR: true,
    });

    const getAllNodeIds = (nodes) => {
        return nodes.reduce((acc, node) => {
            return [...acc, node.id, ...getAllNodeIds(node.children || [])];
        }, []);
    };

    const listToTree = (list) => {
        const map = {}, roots = [], nodeList = JSON.parse(JSON.stringify(list));
        for (let i = 0; i < nodeList.length; i += 1) {
            map[nodeList[i].id] = nodeList[i];
            nodeList[i].children = nodeList[i].children || [];
            nodeList[i].level = 0; // add level property for root nodes
            nodeList[i].transformation = nodeList[i].transformation || []
        }

        for (let i = 0; i < nodeList.length; i += 1) {
            const node = nodeList[i];
            if (node.parent_id !== null && map[node.parent_id]) {
                map[node.parent_id].children.push({...node, level: map[node.parent_id].level + 1});
            } else {
                roots.push(node);
            }
        }

        return roots;
    };

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
            EROSION: false,
            BLUR: false,
        });
        setDialogOpen(false);
    };

    const handleDialogConfirm = () => {
        const selectedTransformations = Object.keys(transformations).filter(key => transformations[key]);
        handleAddNodeContext(newNodeParentId, purposeName, description, selectedTransformations);
        handleDialogClose();
    };

    useEffect(() => {
        setExpanded(getAllNodeIds(treeData));
    }, [treeData]);

    const renderLabel = (node) => {
        const disabled = node.level > 0 && !node.parentSelected;
        const trueTransformations = Object.entries(node.transformation || {})
            .filter(([key, value]) => value)
            .map(([key]) => key);
        return (
            <div style={{display: "flex", flexDirection: "column"}}>
                <div style={{display: "flex", alignItems: "center", justifyContent: "space-between"}}>
                    <div style={{display: "flex", alignItems: "center"}}>
                        {!settingsView && (
                            <Checkbox
                                checked={node.selected}
                                onChange={() => handleCheckboxChange(node.id)}
                                color="primary"
                                disabled={disabled}
                            />
                        )}
                        <div style={{color: disabled ? "grey" : "inherit"}}>{node.name}</div>
                    </div>
                    {settingsView && (
                        <div>
                            <IconButton color="primary" onClick={() => handleAddNode(node.id)}>
                                <AddCircleOutlineIcon/>
                            </IconButton>
                            <IconButton color="secondary" onClick={() => handleDeleteNodeContext(node.id)}>
                                <RemoveCircleOutlineIcon/>
                            </IconButton>
                        </div>
                    )}
                </div>
                <Typography variant="body2" color="textSecondary">{node.description}</Typography>
                <div style={{marginTop: "8px"}}>
                    Transformations:
                    {trueTransformations.map((transformation) => (
                        <Chip key={transformation} label={transformation} color={"primary"}/>
                    ))}
                </div>
            </div>
        );
    };

    const renderTree = (nodes, parentSelected = true) =>
        nodes.map((node) => (
            <TreeItem
                key={node.id}
                nodeId={node.id.toString()}
                label={renderLabel({...node, parentSelected: node.selected && parentSelected})}
            >
                {Array.isArray(node.children) ? renderTree(node.children, node.selected && parentSelected) : null}
            </TreeItem>
        ));

    const treeStructuredData = listToTree(treeData);

    return (
        <div>
            <TreeView
                defaultCollapseIcon={<ArrowDropDownIcon/>}
                defaultExpandIcon={<ArrowRightIcon/>}
                multiSelect
            >
                {renderTree(treeStructuredData)}
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
                    {Object.keys(transformations).map((key) => (
                        <FormControlLabel
                            key={key}
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
